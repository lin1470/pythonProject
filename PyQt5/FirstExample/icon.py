#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 设置位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置标题
        self.setWindowTitle('Icon')
        # 设置标题的图标
        self.setWindowIcon(QIcon('web.png'))
        # 显示
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())