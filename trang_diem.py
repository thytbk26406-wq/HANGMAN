from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from maxscoregiaodien import Ui_Maxscore
from thuvien_max import lay_diem_3_level

_giu = []   # giữ tham chiếu để cửa sổ điểm cao không bị Python xóa mất


# ---------- Trang điểm cao nhất ----------
class ScoreWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Maxscore()
        self.ui.setupUi(self)

        # mũi tên quay lại
        self.ui.btnBack.setIcon(QIcon("mui_ten.png"))

        # hiện điểm cao nhất của 3 level
        easy, medium, hard = lay_diem_3_level()
        self.ui.lbl_diemmaxE.setText(str(easy))
        self.ui.lbl_diemmaxM.setText(str(medium))
        self.ui.lbl_diemmaxH.setText(str(hard))

        self.ui.btnBack.clicked.connect(self.quay_lai)

    def quay_lai(self):
        # tìm trang chọn level (đang bị ẩn) rồi hiện lại
        for w in QtWidgets.QApplication.topLevelWidgets():
            if w.__class__.__name__ == "LevelWindow":
                w.show()
                self.close()
                return
        QtWidgets.QMessageBox.warning(self, "Thông báo", "Không tìm thấy trang chọn level.")


def mo_trang_diem():
    w = ScoreWindow()
    _giu.clear()
    _giu.append(w)
    w.show()