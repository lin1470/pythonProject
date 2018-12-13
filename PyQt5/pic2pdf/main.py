from pic2pdf.ui import MyWidget
from PyQt5.QtWidgets import (QApplication)
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = MyWidget()
    sys.exit(app.exec())