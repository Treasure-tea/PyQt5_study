#Author:-*-coding = utf-8 -*-
#@Time : 2022/4/19 22:01
#@Author : Shenzhi_Yang
#@File : QLabelBuddy.py
#@Software : PyCharm
from PyQt5.QtWidgets import *
import sys

class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')

        nameLabel = QLabel('&Name',self)
        nameLineEdit = QLineEdit(self)
        #设置伙伴关系
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password',self)
        passwordLineEdit = QLineEdit(self)
        #设置伙伴关系
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton("&OK")
        btnCancel = QPushButton("&Cancel")

        mainLayout = QGridLayout(self)
        #mainLayout.addWidget(控件对象，rowIndex,columnIndex,row,column)
        mainLayout.addWidget(nameLabel,0,0)
        mainLayout.addWidget(nameLineEdit,0,1,1,2)

        mainLayout.addWidget(passwordLabel,1,0)
        mainLayout.addWidget(passwordLineEdit,1,1,1,2)

        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancel,2,2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())


