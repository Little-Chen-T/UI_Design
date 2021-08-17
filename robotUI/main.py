import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPalette, QBrush, QPixmap

from Ui_ui import *

class MyClass(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self.setupUi(self)
        self.selectPic.clicked.connect(self.openimage)
 
 
    def openimage(self):

        absPath = os.path.dirname(os.path.abspath(__file__)) #获取当前py文件绝对路径

        jpg = QPixmap(absPath + '\savedImg\source_img.png')

        self.imgLabel.setPixmap(jpg) # 在label上显示图片
        self.imgLabel.setScaledContents (True) # 让图片自适应label大小
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyClass()
    myWin.show()
    sys.exit(app.exec_())
 
