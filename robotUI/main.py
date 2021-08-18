import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPalette, QBrush, QPixmap

from Ui_ui import *

class MyClass(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self.setupUi(self)
        self.drawLine.clicked.connect(self.drawLine)
        self.clearPic.clicked.connect(self.clearImg)
 
 
    def drawLine(self):

        absPath = os.path.dirname(os.path.abspath(__file__)) #获取当前py文件绝对路径

        jpg = QPixmap(absPath + '\drawedImg\source_img.png')

        self.imgLabel.setPixmap(jpg) # 在label上显示图片
        self.imgLabel.setScaledContents (True) # 让图片自适应label大小
    
    def clearImg(self):#清空画图，显示原图

        reply=QMessageBox.question(self,'Message',
                                         '确定要清空吗?',QMessageBox.Yes,
                                         QMessageBox.No)
        if reply==QMessageBox.Yes:
        
            absPath = os.path.dirname(os.path.abspath(__file__)) #获取当前py文件绝对路径

            jpg = QPixmap(absPath + '\srcImg\source_img.png')

            self.imgLabel.setPixmap(jpg) # 在label上显示图片
            self.imgLabel.setScaledContents (True) # 让图片自适应label大小

 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyClass()
    myWin.show()
    sys.exit(app.exec_())
 
