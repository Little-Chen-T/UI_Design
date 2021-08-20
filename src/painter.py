import cv2
import os
import copy
from utils.operation_stack import OperationStack


class Painter:

    """
    绘画对象，实现直线、圆、椭圆、字符等的绘制
    """

    def __init__(self, init_path="img/cache_0.png"):
        
        self.__init_path = init_path
        self.__stack = OperationStack(cv2.imread(self.__init_path))
        self.__color_dic = {0: (0, 0, 255),
                            1: (0, 255, 255),
                            2: (0, 255, 0),
                            3: (0, 97, 255),
                            4: (255, 0, 255),
                            5: (203, 192, 255),
                            6: (255, 255, 0),
                            7: (0, 0, 0),
                            8: (255, 255, 255)}
        self.__screen_width = 1920
        self.__screen_high = 1080

        self.__update()

    def __update(self):
        
        """更新image属性"""

        self.image = self.__stack.front()

    def __convert_color(self, color):

        """
        将通信协议中的对应的颜色转为BGR色彩
        :param:color:   通信协议对应的0-8的颜色,0代表红色
        :return:bgr_color:  对应的bgr颜色
        """
        
        if type(color) is not int:
            color = int(color)
        
        return self.__color_dic[color]

    def __convert_coordinate(self, x, y):
        
        """
        将直角坐标系的坐标转换为OpenCV坐标系中的坐标
        :param:x:   直角坐标系下的x坐标
        :param:y:   直角坐标系下的y坐标
        :return:point:  OpenCV坐标系下的(x, y)坐标
        """
        
        cv_x = self.__screen_high - y;
        cv_y = x;
        point = (cv_y, cv_x)
        return point

    def __write_img(self, image):
        """
        将处理好的图片写入缓存
        :param:image    处理后的cvMat对象
        """

        self.__stack.push(image)
        self.__update()

    def draw_line(self, width, start_x, start_y, end_x, end_y, color):

        """
        在源图像中绘制直线
        :param:width:   线宽
        :param:start_x: 起点x坐标
        :param:start_y: 起点y坐标
        :param:end_x:   终点x坐标
        :param:end_y:   终点y坐标
        :param:color:   颜色
        """
        
        image = copy.deepcopy(self.image)

        color = self.__convert_color(color)
        start_point = self.__convert_coordinate(start_x, start_y)
        end_point = self.__convert_coordinate(end_x, end_y)

        image = cv2.line(image, start_point, end_point, color, width)

        self.__write_img(image)

    def draw_rectangle(self, width, start_x, start_y, end_x, end_y, color):
    
        """
        在源图像中绘制矩形
        :param:width:   线宽
        :param:start_x: 起点x坐标
        :param:start_y: 起点y坐标
        :param:end_x:   对角顶点x坐标
        :param:end_y:   对角顶点y坐标
        :param:color:   颜色
        """
        
        image = copy.deepcopy(self.image)

        color = self.__convert_color(color)
        start_point = self.__convert_coordinate(start_x, start_y)
        end_point = self.__convert_coordinate(end_x, end_y)

        image = cv2.rectangle(image, start_point, end_point, color, width)

        self.__write_img(image)

    def draw_circle(self, width, center_x, center_y, radius, color):
        
        """
        在源图像中绘制圆形
        :param:width:   线宽
        :param:center_x:    圆心x坐标
        :param:center_y:    圆心y坐标
        :param:radius:  圆的半径
        :param:color:   颜色
        """
        
        image = copy.deepcopy(self.image)

        color = self.__convert_color(color)
        center_point = self.__convert_coordinate(center_x, center_y)

        image = cv2.circle(image, center_point, radius, color, width)

        self.__write_img(image)

    def draw_ellipse(self, width, center_x, center_y, length_x, length_y, color):
        
        """
        在源图像中绘制圆形
        :param:width:   线宽
        :param:center_x:    圆心x坐标
        :param:center_y:    圆心y坐标
        :param:length_x:    x半轴长度
        :param:length_y:    y半轴长度
        :param:color:   颜色
        """
        
        image = copy.deepcopy(self.image)

        color = self.__convert_color(color)
        center_point = self.__convert_coordinate(center_x, center_y)

        image = cv2.ellipse(image, center_point, (length_x, length_y), 0, 360, 0, color, width)

        self.__write_img(image)
    
    def draw_text(self, size, width, start_x, start_y, text, color):

        """
        在源图像中绘制字符
        :parma:size:    字体大小
        :param:width:   线宽
        :param:start_x:    字符左下角x坐标
        :param:start_y:    字符左下角y坐标
        :param:text:   文本内容
        :param:color:   文本颜色
        """

        image = copy.deepcopy(self.image)

        color = self.__convert_color(color)
        point = self.__convert_coordinate(start_x, start_y)

        image = cv2.putText(image, text, point, cv2.FONT_HERSHEY_SIMPLEX, size, color, width)

        self.__write_img(image)

    def rollback(self):

        """撤销操作"""

        self.__stack.rollback()
        self.__update()

    def recover(self):

        """恢复操作"""

        self.__stack.recover()
        self.__update()

    def clear(self):

        """清空操作"""

        self.__stack = OperationStack(cv2.imread(self.__init_path))
        self.__update()

    def save(self):

        """保存当前图片"""

        cv2.imwrite("img/cache_1.png", self.image)

if __name__ == "__main__":

    painter = Painter()
    painter.draw_line(10, 10, 10, 100, 100, 1)
    painter.rollback()
    painter.draw_rectangle(10, 200, 200, 300, 300, 0)
    # painter.draw_circle(10, 500, 500, 2, 3)
    # painter.draw_ellipse(10, 700, 700, 200, 400, 5)
    painter.save()