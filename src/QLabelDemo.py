#Author:-*-coding = utf-8 -*-
#@Time : 2022/4/18 21:26
#@Author : Shenzhi_Yang
#@File : QLabelDemo.py
#@Software : PyCharm
import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication,QPushButton,QWidget,QLabel,QVBoxLayout
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt
class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签.</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./images/python.jpg"))

        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注《Python从菜鸟到高手》</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级链接')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel控件演示")


    def linkHovered(self):
        print("当鼠标滑过label2标签时，触发事件")

    def linkClicked(self):
        print('当鼠标滑过label4标签时，触发事件')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
