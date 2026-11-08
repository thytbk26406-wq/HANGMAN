import sys
from PyQt6.QtWidgets import QApplication
from test_lv2 import Hangman


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Hangman()
    game.show()
    sys.exit(app.exec())
