import sys, os, json, hashlib
os.environ["QT_SCALE_FACTOR"] = "0.8"   # thu nhỏ giao diện cho vừa màn hình (muốn nhỏ hơn thì giảm số)
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtGui import QIcon, QPixmap, QPainter, QPen, QColor

FILE = "accounts.json"
LOI_MK = "Mật khẩu ít nhất 8 ký tự, 1 chữ cái in hoa, 1 số, 1 ký tự đặc biệt"
STYLE_NUT = ("QPushButton {background-color:#0780C3; color:white; border-radius:14px;"
             "font-size:16pt; font-weight:bold;} QPushButton:hover {background-color:#0A93E0;}")


# ---------- Các hàm ----------
def doc_tk():
    if os.path.exists(FILE):
        with open(FILE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def luu_tk(ds):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(ds, f)


def bam(mk):
    return hashlib.sha256(mk.encode()).hexdigest()   # không lưu mật khẩu dạng chữ thường


def mat_khau_manh(mk):
    hoa = so = dac_biet = False
    for c in mk:                       # vòng for duyệt từng ký tự
        if c.isupper():
            hoa = True
        elif c.isdigit():
            so = True
        elif not c.isalnum():
            dac_biet = True
    return len(mk) >= 8 and hoa and so and dac_biet


def ve_mat(gach):                      # vẽ con mắt bằng hình cơ bản
    pm = QPixmap(96, 96)
    pm.fill(Qt.GlobalColor.transparent)
    p = QPainter(pm)
    p.setRenderHint(QPainter.RenderHint.Antialiasing)
    p.setPen(QPen(QColor("#01579B"), 7))
    p.drawEllipse(8, 26, 80, 44)       # tròng mắt
    p.setBrush(QColor("#01579B"))
    p.drawEllipse(36, 36, 24, 24)      # con ngươi
    if gach:
        p.drawLine(14, 84, 82, 12)     # gạch chéo khi đang ẩn
    p.end()
    return QIcon(pm)


def them_con_mat(o):
    o.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
    nut = QtWidgets.QToolButton(o)
    nut.setIcon(ve_mat(True))
    nut.setIconSize(QSize(36, 36))
    nut.setStyleSheet("border: none;")
    nut.setGeometry(o.width() - 60, (o.height() - 40) // 2, 40, 40)

    def doi():
        an = o.echoMode() == QtWidgets.QLineEdit.EchoMode.Password
        o.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal if an else QtWidgets.QLineEdit.EchoMode.Password)
        nut.setIcon(ve_mat(not an))

    nut.clicked.connect(doi)


def tao_loi(cua_so, nut):              # label đỏ nằm dưới nút
    lbl = QtWidgets.QLabel(cua_so)
    lbl.setGeometry(0, nut.y() + nut.height() + 5, cua_so.width(), 40)
    lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
    lbl.setStyleSheet("color: red; font-size: 13pt; font-weight: bold;")
    cua_so.resize(cua_so.width(), lbl.y() + 50)
    return lbl


def cai_dat(cua_so, nut, cac_o):
    """Gán màu nút, tạo label lỗi, xóa lỗi khi gõ lại, Enter nhảy sang ô kế."""
    nut.setStyleSheet(STYLE_NUT)
    cua_so.lblError = tao_loi(cua_so, nut)
    for i in range(len(cac_o)):
        cac_o[i].textEdited.connect(lambda: cua_so.lblError.setText(""))
        if i < len(cac_o) - 1:
            cac_o[i].returnPressed.connect(cac_o[i + 1].setFocus)
        else:
            cac_o[i].returnPressed.connect(nut.click)


def thong_bao_thanh_cong(cha, noi_dung):
    h = QtWidgets.QDialog(cha, Qt.WindowType.FramelessWindowHint)
    h.setStyleSheet("background:#43A047; color:white; font-size:18pt; font-weight:bold;")
    tick = QtWidgets.QLabel("✓")
    tick.setFixedSize(50, 50)
    tick.setAlignment(Qt.AlignmentFlag.AlignCenter)
    tick.setStyleSheet("background:white; color:#43A047; border-radius:25px; font-size:28pt;")
    bo_cuc = QtWidgets.QHBoxLayout(h)
    bo_cuc.setContentsMargins(40, 30, 40, 30)
    bo_cuc.addWidget(tick)
    bo_cuc.addWidget(QtWidgets.QLabel(noi_dung))
    QTimer.singleShot(1500, h.accept)   # tự đóng sau 1,5 giây
    h.exec()


# ---------- Trang chủ ----------
class WelcomeWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("welcome.ui", self)
        self.btnLogin.clicked.connect(lambda: self.mo(LoginWindow))
        self.btnRegister.clicked.connect(lambda: self.mo(RegisterWindow))

    def mo(self, trang):
        self.trang = trang()
        self.trang.show()
        self.close()


# ---------- Trang đăng ký ----------
class RegisterWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("register.ui", self)
        cai_dat(self, self.btnRegister, [self.txtUsername, self.txtPassword, self.txtConfirm])
        them_con_mat(self.txtPassword)
        them_con_mat(self.txtConfirm)
        self.btnRegister.clicked.connect(self.dang_ky)
        self.btnBack.clicked.connect(self.quay_lai)

    def dang_ky(self):
        user = self.txtUsername.text().strip()
        mk = self.txtPassword.text()
        ds = doc_tk()
        if user == "":
            self.lblError.setText("Vui lòng nhập tên đăng nhập")
        elif user in ds:
            self.lblError.setText("Tên đăng nhập đã tồn tại")
        elif not mat_khau_manh(mk):
            self.lblError.setText(LOI_MK)
        elif mk != self.txtConfirm.text():
            self.lblError.setText("Mật khẩu không khớp")
        else:
            ds[user] = bam(mk)
            luu_tk(ds)
            thong_bao_thanh_cong(self, "Đăng ký thành công!")
            self.trang = LoginWindow()
            self.trang.show()
            self.close()

    def quay_lai(self):
        self.trang = WelcomeWindow()
        self.trang.show()
        self.close()


# ---------- Trang trắng (tạm, chờ phần game) ----------
class TrangTrang(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")


# ---------- Trang đăng nhập ----------
class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)
        cai_dat(self, self.btnLogin, [self.txtUsername, self.txtPassword])
        them_con_mat(self.txtPassword)
        self.btnLogin.clicked.connect(self.dang_nhap)
        self.btnBack.clicked.connect(self.quay_lai)

    def dang_nhap(self):
        user = self.txtUsername.text().strip()
        ds = doc_tk()
        if user in ds and ds[user] == bam(self.txtPassword.text()):
            self.trang = TrangTrang()      # TODO: thay bằng màn hình game
            self.trang.showMaximized()
            self.close()
        else:
            self.lblError.setText("Tên đăng nhập hoặc mật khẩu không chính xác")

    def quay_lai(self):
        self.trang = WelcomeWindow()
        self.trang.show()
        self.close()


app = QtWidgets.QApplication(sys.argv)
window = WelcomeWindow()
window.show()
sys.exit(app.exec())