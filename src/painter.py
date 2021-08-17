import cv2
import os


class Painter:

    """
    绘画对象，实现直线、圆、椭圆、字符等的绘制
    """

    def __init__(self):

        self.__path_input_img = "img/source_img.png"
        self.__path_cache_img = "img/cache_img.png"
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
        # self.path_output_img = "/img/output_img.png"
        # self.source_img = cv2.imread(self.path_source_img)

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

    def __load_img(self):
        
        """
        加载图像。若没有缓存图片，加载原图；若有，加载缓存图片。
        :return:image  读取到的图片
        """

        if os.path.exists(self.__path_cache_img):
            image = cv2.imread(self.__path_cache_img)
        else:
            image = cv2.imread(self.__path_input_img)

        return image



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
        
        image = self.__load_img()

        color = self.__convert_color(color)
        start_point = self.__convert_coordinate(start_x, start_y)
        end_point = self.__convert_coordinate(end_x, end_y)

        image = cv2.line(image, start_point, end_point, color, width)

        cv2.imwrite(self.__path_cache_img, image)

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
        
        image = self.__load_img()

        color = self.__convert_color(color)
        start_point = self.__convert_coordinate(start_x, start_y)
        end_point = self.__convert_coordinate(end_x, end_y)

        image = cv2.rectangle(image, start_point, end_point, color, width)

        cv2.imwrite(self.__path_cache_img, image)

    def draw_circle(self, width, center_x, center_y, radius, color):
        
        """
        在源图像中绘制圆形
        :param:width:   线宽
        :param:center_x:    圆心x坐标
        :param:center_y:    圆心y坐标
        :param:radius:  圆的半径
        :param:color:   颜色
        """
        
        image = self.__load_img()

        color = self.__convert_color(color)
        center_point = self.__convert_coordinate(center_x, center_y)

        image = cv2.circle(image, center_point, radius, color, width)

        cv2.imwrite(self.__path_cache_img, image)

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
        
        image = self.__load_img()

        color = self.__convert_color(color)
        center_point = self.__convert_coordinate(center_x, center_y)

        image = cv2.ellipse(image, center_point, length_x, length_y, color, width)

        cv2.imwrite(self.__path_cache_img, image)


if __name__ == "__main__":

    # painter = Painter()
    # painter.draw_line(10, 10, 10, 100, 100, 1)
    # painter.draw_rectangle(10, 200, 200, 300, 300, 0)
    # painter.draw_circle(10, 500, 500, 2, 3)
    # painter.draw_ellipse(10, 700, 700, 100, 50, 5)