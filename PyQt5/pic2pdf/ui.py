#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QFileDialog, QMessageBox)
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QGridLayout, QApplication,QPushButton)
import sys
from pic2pdf.pic2pdf import Solution

class TypeButton(QPushButton):
    def __init__(self,text,type):
        super().__init__()
        # 如果type=1,则是picButton,如果是2是storeButton
        self.type = type
        self.setText(text)

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.picPathEdit = QLineEdit()
        self.storePathEdit = QLineEdit()
        self.picBt = TypeButton("Browse",1)
        self.storeBt = TypeButton("Browse",2)
        self.picBt.clicked.connect(self.getFilePath)
        self.storeBt.clicked.connect(self.getFilePath)
        runButton = QPushButton("Run")
        runButton.clicked.connect(self.runFunc)
        picLabel = QLabel("请选择要转换的图片路径:")
        storeLabel = QLabel("请选择要保存的路径:")
        grid = QGridLayout()
        grid.setSpacing(5)
        grid.addWidget(picLabel,0,0,1,2)
        grid.addWidget(self.picPathEdit,1,0)
        grid.addWidget(self.picBt,1,1)
        grid.addWidget(storeLabel,2,0)
        grid.addWidget(self.storePathEdit,3,0)
        grid.addWidget(self.storeBt,3,1)
        grid.addWidget(runButton,4,0)
        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('pics2pdf')
        self.show()

    def getFilePath(self):
        fileDia = QFileDialog()
        fname = QFileDialog.getExistingDirectory(self,'select dir','.')
        print(fname)
        sender = self.sender()
        if sender.type == 1:
            self.picPathEdit.setText(fname)
        elif sender.type == 2:
            self.storePathEdit.setText(fname)

    def runFunc(self):
        print(type(self.picPathEdit.text()))
        picPath = self.picPathEdit.text()
        storePath = self.storePathEdit.text()
        # 利用提示对话框停止操作
        if picPath=='' or  storePath == '':
            messageBox = QMessageBox(QMessageBox.Warning,"提示",'请先选择路径',QMessageBox.Close,self)
            messageBox.show()
        else:
            solution = Solution()
            solution.setPicPath(picPath)
            solution.setStorePath(storePath)
            solution.travelFiles()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = MyWidget()
    sys.exit(app.exec())