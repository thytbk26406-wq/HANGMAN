import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMessageBox
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import pyqtSignal

from gd_hangman import Ui_Form
from xuli import HangmanLogic

from maxscoregiaodien import Ui_Maxscore
from thuvien_max import luu_diem, lay_diem_3_level


class MaxScore(QWidget):
    """Màn hình điểm cao nhất, dùng giao diện Ui_Maxscore"""

    def __init__(self):
        super().__init__()
        self.ui = Ui_Maxscore()
        self.ui.setupUi(self)

    def cap_nhat(self):
        """Lấy điểm cao nhất từ thuvien_max rồi hiển thị lên 3 ô level"""
        easy, medium, hard = lay_diem_3_level()
        self.ui.lbl_diemmaxE.setText(str(easy))
        self.ui.lbl_diemmaxM.setText(str(medium))
        self.ui.lbl_diemmaxH.setText(str(hard))


class Hangman(QWidget):
    ket_thuc = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Tên cấp độ dùng để lưu điểm cao nhất của Level 3
        self.level_name = "Hard"
        self.max_window = None

        # Khi chơi hết các từ thì lưu điểm và mở bảng điểm
        self.ket_thuc.connect(self.on_hoan_thanh)

        # Khởi tạo đối tượng xử lý từ tệp xuli.py
        self.logic = HangmanLogic()

        # Chỉnh font và kiểu dáng chữ cho tiêu đề
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

        # Tạo nhãn Level 3 và Điểm số
        self.level_label = QLabel("LEVEL 3: Hard", self)
        self.level_label.setGeometry(40, 65, 200, 20)
        self.level_label.setStyleSheet("font-size: 15px; color: #01579B; font-weight: bold; background-color: transparent;")
        self.level_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.score_label = QLabel(self)
        self.score_label.setGeometry(310, 20, 200, 22)
        self.score_label.setStyleSheet("font-size: 13px; color: #01579B; font-weight: bold; background-color: transparent;")
        self.score_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Khai báo danh sách chứa 26 nút bấm chữ cái
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

        # Khai báo danh sách 6 trái tim
        self.hearts = [
            self.ui.label_3, self.ui.label_4, self.ui.label_7,
            self.ui.label_8, self.ui.label_5, self.ui.label_6
        ]

        # Khởi tạo 6 bộ phận người treo cổ
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

    def restart_game(self):
        self.logic.reset_game()
        self.next_word()

    def next_word(self):
        has_next = self.logic.prepare_next_word()

        if not has_next:
            # Đã chơi hết danh sách từ -> kết thúc level
            self.update_score()
            QMessageBox.information(
                self, "Hoàn thành Level",
                f"Chúc mừng! Tổng điểm: {self.logic.score}"
            )
            self.ket_thuc.emit(self.logic.score)
            return

        for p in self.parts:
            p.hide()

        for h in self.hearts:
            h.setText("❤️")
            h.setStyleSheet("color: red; font-size: 18px;")

        self.ui.label_15.setText("Gợi ý: " + self.logic.hint)
        self.ui.label_14.setText(self.logic.get_display_text())

        for b in self.buttons:
            b.setEnabled(True)

        self.update_score()

    def update_score(self):
        round_info = f"Điểm: {self.logic.score}  |  Vòng: {self.logic.get_current_round()}/{self.logic.get_total_words()}"
        self.score_label.setText(round_info)

    def click_btn(self):
        btn = self.sender()
        btn.setEnabled(False)

        letter = btn.text()
        is_correct, is_win = self.logic.process_guess(letter)

        if is_correct:
            self.ui.label_14.setText(self.logic.get_display_text())
            if is_win:
                self.update_score()
                self.next_word()
        else:
            wrong_count = self.logic.get_wrong_count()
            if 1 <= wrong_count <= 6:
                self.parts[wrong_count - 1].show()
                self.hearts[wrong_count - 1].setText("♡")

            if self.logic.lives == 0:
                # Hết lượt đoán -> lưu điểm vào thư viện trước khi hỏi
                luu_diem(self.level_name, self.logic.score)

                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setWindowTitle("BẠN ĐÃ HẾT LƯỢT ĐOÁN")
                msg.setText(f"Từ đúng: {self.logic.secret_word}\nTổng điểm: {self.logic.score}")

                btn_retry = msg.addButton("Thử lại", QMessageBox.ButtonRole.AcceptRole)
                msg.addButton("Thoát", QMessageBox.ButtonRole.RejectRole)

                msg.exec()

                if msg.clickedButton() == btn_retry:
                    self.restart_game()
                else:
                    self.mo_bang_diem()

    def on_hoan_thanh(self, diem):
        """Chơi hết các từ -> lưu điểm và mở bảng điểm"""
        luu_diem(self.level_name, diem)
        self.mo_bang_diem()

    def mo_bang_diem(self):
        """Mở màn hình Max Score, cập nhật điểm mới nhất rồi ẩn màn hình game"""
        if self.max_window is None:
            self.max_window = MaxScore()
            self.max_window.ui.btnBack.clicked.connect(self.quay_lai)
        self.max_window.cap_nhat()
        self.max_window.show()
        self.hide()

    def quay_lai(self):
        """Nút back trên màn hình điểm: quay lại game và chơi lại từ đầu"""
        self.max_window.hide()
        self.restart_game()
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Hangman()
    game.show()
    sys.exit(app.exec())