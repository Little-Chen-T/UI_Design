import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QIcon

from Ui_ui import *
from src.painter import *
import src.painter

from ui_utils.imgCvt import*

class MyClass(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self.setupUi(self)

        #设置主界面图标
        self.setWindowIcon(QIcon(os.path.dirname(os.path.abspath(__file__)) + '/icon/icon.png'));
        
        #初始化参数
        self.initPara()

        #直线，矩形，圆，椭圆，字符串
        self.drawLine.clicked.connect(self.drawLineFun)
        self.drawRect.clicked.connect(self.drawRectFun)
        self.drawCircle.clicked.connect(self.drawCircleFun)
        self.drawEllipse.clicked.connect(self.drawEllipseFun)
        self.drawStr.clicked.connect(self.drawStrFun)

        #清空
        self.clearPic.clicked.connect(self.clearImg)

        #保存图片
        self.saveImg.clicked.connect(painter.save)

        #前进后退
        self.forward.clicked.connect(self.nextImg)
        self.backwards.clicked.connect(self.lastImg)

        #生成代码
        # self.genCode.clicked.connect(painter.printStack2)
    
    #初始化参数
    def initPara(self):

        #显示原始图片
        absPath = os.path.dirname(os.path.abspath(__file__)) #获取当前py文件绝对路径

        jpg = QPixmap(absPath + '\srcImg\source_img.png')

        self.imgLabel.setPixmap(jpg) # 在label上显示图片
        self.imgLabel.setScaledContents (True) # 让图片自适应label大小

        #直线参数
        self.lineWidth.setPlainText("1")
        self.lineStartXY.setPlainText("0 0")
        self.lineEndXY.setPlainText("0 0")
        self.lineColor.setPlainText("0")

        #直线矩形
        self.rectWidth.setPlainText("1")
        self.rectStartXY.setPlainText("0 0")
        self.rectEndXY.setPlainText("0 0")
        self.rectColor.setPlainText("0")

        #直线圆
        self.circleWidth.setPlainText("1")
        self.circleCenter.setPlainText("0 0")
        self.circleR.setPlainText("1")
        self.circleColor.setPlainText("0")

        #直线椭圆
        self.ellipseWidth.setPlainText("1")
        self.ellipseCenter.setPlainText("0 0")
        self.ellipseXY.setPlainText("0 0")
        self.ellipseColor.setPlainText("0")

        #直线字符
        self.strSize.setPlainText("1")
        self.strWidth.setPlainText("1")
        self.strStartXY.setPlainText("0 0")
        self.strContent.setPlainText("SPR")
        self.strColor.setPlainText("0")

    #画直线
    def drawLineFun(self):

        #从text中读取参数
        lineWidth_s = self.lineWidth.toPlainText()
        lineStartX_s = self.lineStartXY.toPlainText().strip().split(' ')[0] #先去掉两边空格，再得到数字，然后在下面画图函数中用replace替换所有空格
        lineStartY_s = self.lineStartXY.toPlainText().strip().split(' ')[-1]
        lineEndX_s = self.lineEndXY.toPlainText().strip().split(' ')[0]
        lineEndY_s = self.lineEndXY.toPlainText().strip().split(' ')[-1]
        color_s = self.lineColor.toPlainText()

        painter.draw_line(int(lineWidth_s.replace(" ", "")), int(lineStartX_s.replace(" ", "")), int(lineStartY_s.replace(" ", "")), int(lineEndX_s.replace(" ", "")), int(lineEndY_s.replace(" ", "")), int(color_s.replace(" ", "")) % 9)

        jpg = mat2qpix(painter.image) # mat to qpixmap

        self.imgLabel.setPixmap(jpg) # 在label上显示图片
        self.imgLabel.setScaledContents (True) # 让图片自适应label大小

    #画矩形
    def drawRectFun(self):
    
        #从text中读取参数
        rectWidth_s = self.rectWidth.toPlainText()
        rectStartX_s = self.rectStartXY.toPlainText().strip().split(' ')[0] #先去掉两边空格，再得到数字，然后在下面画图函数中用replace替换所有空格
        rectStartY_s = self.rectStartXY.toPlainText().strip().split(' ')[-1]
        rectEndX_s = self.rectEndXY.toPlainText().strip().split(' ')[0]
        rectEndY_s = self.rectEndXY.toPlainText().strip().split(' ')[-1]
        color_s = self.rectColor.toPlainText()

        painter.draw_rectangle(int(rectWidth_s.replace(" ", "")), int(rectStartX_s.replace(" ", "")), int(rectStartY_s.replace(" ", "")), int(rectEndX_s.replace(" ", "")), int(rectEndY_s.replace(" ", "")), int(color_s.replace(" ", "")) % 9)

        jpg = mat2qpix(painter.image) # mat to qpixmap

        self.imgLabel.setPixmap(jpg) # 在label上显示图片
        self.imgLabel.setScaledContents (True) # 让图片自适应label大小

    def drawCircleFun(self):
    
        #从text中读取参数
        circleWidth_s = self.circleWidth.toPlainText()
        circleCenterX_s = self.circleCenter.toPlainText().strip().split(' ')[0] #先去掉两边空格，再得到数字，然后在下面画图函数中用replace替换所有空格
        circleCenterY_s = self.circleCenter.toPlainText().strip().split(' ')[-1]
        circleR_s = self.circleR.toPlainText().strip().split(' ')[0]
        color_s = self.circleColor.toPlainText()

        painter.draw_circle(int(circleWidth_s.replace(" ", "")), int(circleCenterX_s.replace(" ", "")), int(circleCenterY_s.replace(" ", "")), int(circleR_s.replace(" ", "")), int(color_s.replace(" ", "")) % 9)

        jpg = mat2qpix(painter.image) # mat to qpixmap

        self.imgLabel.setPixmap(jpg) # 在label上显示图片
        self.imgLabel.setScaledContents (True) # 让图片自适应label大小

    def drawEllipseFun(self):
    
        #从text中读取参数
        ellipseWidth_s = self.ellipseWidth.toPlainText()
        ellipseCenterX_s = self.ellipseCenter.toPlainText().strip().split(' ')[0] #先去掉两边空格，再得到数字，然后在下面画图函数中用replace替换所有空格
        ellipseCenterY_s = self.ellipseCenter.toPlainText().strip().split(' ')[-1]
        ellipseX_s = self.ellipseXY.toPlainText().strip().split(' ')[0]
        ellipseY_s = self.ellipseXY.toPlainText().strip().split(' ')[-1]
        color_s = self.ellipseColor.toPlainText()

        painter.draw_ellipse(int(ellipseWidth_s.replace(" ", "")), int(ellipseCenterX_s.replace(" ", "")), int(ellipseCenterY_s.replace(" ", "")), int(ellipseX_s.replace(" ", "")), int(ellipseY_s.replace(" ", "")), int(color_s.replace(" ", "")) % 9)

        jpg = mat2qpix(painter.image) # mat to qpixmap

        self.imgLabel.setPixmap(jpg) # 在label上显示图片
        self.imgLabel.setScaledContents (True) # 让图片自适应label大小

    #画字符
    def drawStrFun(self):
    
        #从text中读取参数
        strSize_s = self.strSize.toPlainText()
        strWidth_s = self.strWidth.toPlainText()
        strStartX_s = self.strStartXY.toPlainText().strip().split(' ')[0]
        strStartY_s = self.strStartXY.toPlainText().strip().split(' ')[-1]
        strContent_s = self.strContent.toPlainText()
        color_s = self.strColor.toPlainText()

        painter.draw_text(int(strSize_s.replace(" ", "")), int(strWidth_s.replace(" ", "")), int(strStartX_s.replace(" ", "")), int(strStartY_s.replace(" ", "")), strContent_s, int(color_s.replace(" ", "")) % 9)

        jpg = mat2qpix(painter.image) # mat to qpixmap

        self.imgLabel.setPixmap(jpg) # 在label上显示图片
        self.imgLabel.setScaledContents (True) # 让图片自适应label大小
    
    def clearImg(self):#清空画图，显示原图

        reply=QMessageBox.question(self,'Message',
                                         '确定要清空吗?',QMessageBox.Yes,
                                         QMessageBox.No)
        if reply==QMessageBox.Yes:
        
            painter.clear()
            jpg = mat2qpix(painter.image)

            self.imgLabel.setPixmap(jpg) # 在label上显示图片
            self.imgLabel.setScaledContents (True) # 让图片自适应label大小

    def lastImg(self): #后退

        painter.rollback()
        
        jpg = mat2qpix(painter.image) # mat to qpixmap

        self.imgLabel.setPixmap(jpg) # 在label上显示图片
        self.imgLabel.setScaledContents (True) # 让图片自适应label大小

    
    def nextImg(self): #前进
    
        painter.recover()
        
        jpg = mat2qpix(painter.image) # mat to qpixmap

        self.imgLabel.setPixmap(jpg) # 在label上显示图片
        self.imgLabel.setScaledContents (True) # 让图片自适应label大小
 
 
if __name__ == '__main__':
    painter = Painter()
    app = QApplication(sys.argv)
    myWin = MyClass()
    myWin.show()
    sys.exit(app.exec_())
 
