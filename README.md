# UI_Design

## 文件树

```shell
│  README.md             -- 项目ReadMe文档
│  
├─img                    -- 存放图片资源
│      source_img.png
│      
└─src                    -- 存放代码源文件
```

## 第一版

### 实现思路

初步实现静态绘图，即前端发出绘图指令，后端调用OpenCV实现读取原图、绘制新图、保存图片，再在前端界面对图片进行展示。

前端提供若干绘图选项（按钮形式）：

- 直线
- 矩形
- 圆
- 椭圆
- 字符

对应不同的绘图选项要给出不同的参数输入框：

- 直线：线条宽度、起点x坐标、起点y坐标、终点x坐标、终点y坐标、颜色
- 矩形：线条宽度、起点x坐标、起点y坐标、对角顶点x坐标、对角顶点y坐标、颜色
- 圆：线条宽度、圆心x坐标、圆心y坐标、半径、颜色
- 椭圆：线条快读、圆心x坐标、圆心y坐标、x半轴长度、y半轴长度、颜色
- 字符：字体大小、线条宽度、起点x坐标、起点y坐标

### 更新记录
