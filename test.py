import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMessageBox
from PyQt6 import QtCore, QtGui
from gd_hangman import Ui_Form
from word_data import word_list, hint_list
from thuvien_max import luu_diem


class Hangman(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Kiểm tra điểm đã được lưu hay chưa
        self.score_saved = False

        # Kiểm tra trang điểm cao đã được mở chưa
        self.score_page_opened = False

        #Chỉnh font và kiểu dáng chữ cho tiêu đề
        font_bold = QtGui.QFont()
        font_bold.setBold(True)
        font_bold.setPointSize(14)

        lbl_style = "color: #01579B; background-color: transparent; border: none; font-weight: bold;"

        self.ui.label_13.setFont(font_bold)
        self.ui.label_13.setStyleSheet(lbl_style)
        self.ui.label_13.setGeometry(10, 8, 101, 35)

        self.ui.label_14.setFont(font_bold)
        self.ui.label_14.setStyleSheet(lbl_style)
        self.ui.label_14.setGeometry(10, 5, 171, 41)

        self.ui.label_15.setFont(font_bold)
        self.ui.label_15.setStyleSheet(lbl_style)
        self.ui.label_15.setGeometry(10, 5, 171, 41)

        #Tạo nhãn Level và Điểm số
        self.level_label = QLabel("LEVEL 1: Easy", self)
        self.level_label.setGeometry(40, 65, 200, 20)
        self.level_label.setStyleSheet("font-size: 15px; color: #01579B; font-weight: bold; background-color: transparent;")
        self.level_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.score_label = QLabel(self)
        self.score_label.setGeometry(310, 20, 200, 22)
        self.score_label.setStyleSheet("font-size: 13px; color: #01579B; font-weight: bold; background-color: transparent;")
        self.score_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        #Khai báo danh sách chứa 26 nút bấm trực tiếp
        self.buttons = [
            self.ui.pushButton, self.ui.pushButton_2, self.ui.pushButton_3, self.ui.pushButton_4,
            self.ui.pushButton_5, self.ui.pushButton_6, self.ui.pushButton_7, self.ui.pushButton_8,
            self.ui.pushButton_9, self.ui.pushButton_10, self.ui.pushButton_11, self.ui.pushButton_12,
            self.ui.pushButton_13, self.ui.pushButton_14, self.ui.pushButton_15, self.ui.pushButton_16,
            self.ui.pushButton_17, self.ui.pushButton_18, self.ui.pushButton_19, self.ui.pushButton_20,
            self.ui.pushButton_21, self.ui.pushButton_22, self.ui.pushButton_23, self.ui.pushButton_24,
            self.ui.pushButton_25, self.ui.pushButton_26
        ]

        for btn in self.buttons:
            btn.clicked.connect(self.click_btn)

        #Khai báo danh sách 6 trái tim
        self.hearts = [
            self.ui.label_3, self.ui.label_4, self.ui.label_7,
            self.ui.label_8, self.ui.label_5, self.ui.label_6
        ]

        #Khởi tạo 6 bộ phận người treo cổ
        self.parts = []
        part_configs = [
            (95, 55, 30, 30, "border: 4px solid #0288D1; border-radius: 15px;"),
            (108, 84, 5, 55, "background-color: #0288D1;"),
            (85, 95, 27, 5, "background-color: #0288D1;"),
            (112, 95, 27, 5, "background-color: #0288D1;"),
            (91, 135, 22, 5, "background-color: #0288D1;"),
            (108, 135, 22, 5, "background-color: #0288D1;")
        ]

        for config in part_configs:
            p = QLabel(self.ui.frame_2)
            p.setGeometry(config[0], config[1], config[2], config[3])
            p.setStyleSheet(config[4])
            p.hide()
            self.parts.append(p)

        self.restart_game()

    # Hàm lưu điểm Level 1
    def save_score(self):
        if not self.score_saved:
            luu_diem("Easy", self.score)
            self.score_saved = True

    # Kết thúc game: đóng cửa sổ, closeEvent sẽ lưu điểm và mở trang điểm cao
    def mo_diem_cao(self):
        self.close()

    def restart_game(self):
        self.remaining_indices = []
        for i in range(len(word_list)):
            self.remaining_indices.append(i)

        self.score = 0
        self.score_saved = False
        self.next_word()

    def next_word(self):
        if len(self.remaining_indices) == 0:
            self.save_score()
            self.update_score()
            QMessageBox.information(
                self,
                "Hoàn thành Level",
                f"Chúc mừng! Bạn đã chinh phục tất cả các từ vựng!\nTổng điểm đạt được: {self.score}"
            )
            self.mo_diem_cao()
            return

        random_pos = random.randint(0, len(self.remaining_indices) - 1)
        chosen_index = self.remaining_indices.pop(random_pos)
        self.secret_word = word_list[chosen_index]
        self.hint = hint_list[chosen_index]

        self.lives = 6
        self.guessed_letters = []

        for p in self.parts:
            p.hide()

        for h in self.hearts:
            h.setText("❤️")
            h.setStyleSheet("color: red; font-size: 18px;")

        self.ui.label_15.setText("Gợi ý: " + self.hint)
        self.update_word_display()

        for b in self.buttons:
            b.setEnabled(True)

        self.update_score()

    def update_score(self):
        self.score_label.setText(f"Điểm: {self.score}  |  Vòng: {len(word_list) - len(self.remaining_indices)}/{len(word_list)}")

    def update_word_display(self):
        display_text = ""
        for i in range(len(self.secret_word)):
            char = self.secret_word[i]
            if char in self.guessed_letters:
                display_text += char
            else:
                display_text += "_"

            if i < len(self.secret_word) - 1:
                display_text += " "

        self.ui.label_14.setText(display_text)

    def click_btn(self):
        btn = self.sender()
        btn.setEnabled(False)

        if btn.text() in self.secret_word:
            self.guessed_letters.append(btn.text())
            self.update_word_display()
        else:
            self.lives -= 1
            wrong_count = 6 - self.lives
            if 1 <= wrong_count <= 6:
                self.parts[wrong_count - 1].show()
                self.hearts[wrong_count - 1].setText("♡")

        #Kiểm tra điều kiện thắng
        win = True
        for char in self.secret_word:
            if char not in self.guessed_letters:
                win = False
                break

        if win:
            self.score += 1
            self.update_score()
            self.next_word()
        elif self.lives == 0:
            QMessageBox.information(
                self,
                "BẠN ĐÃ HẾT LƯỢT ĐOÁN",
                f"Từ đúng: {self.secret_word}\n"
                f"Tổng điểm: {self.score}"
            )

            # Hết lượt thì sang trang điểm cao nhất
            self.mo_diem_cao()

    # Mọi cách thoát game (hết từ, hết lượt, bấm nút X) đều lưu điểm rồi mở trang điểm cao
    def closeEvent(self, event):
        self.save_score()
        if not self.score_page_opened:
            self.score_page_opened = True
            try:
                from trang_diem import mo_trang_diem
                mo_trang_diem()
            except Exception:
                import traceback
                QMessageBox.critical(self, "Lỗi mở trang điểm cao", traceback.format_exc())
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Hangman()
    game.show()
    sys.exit(app.exec())