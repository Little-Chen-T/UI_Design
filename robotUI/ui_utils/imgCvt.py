import cv2
import numpy as np
from PyQt5.QtGui import *
from PyQt5 import QtGui

def mat2qpix(cvimg):

    height, width, depth = cvimg.shape
    cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
    qimg = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)

    Pixmap = QtGui.QPixmap.fromImage(qimg)

    return Pixmap
