# UI_Design

## 文件树

```shell
│  .gitignore
│  README.md
│  tree.txt
│  
├─.qt_for_python
│  └─uic
│          ui.py
│          
├─.vscode
│      launch.json
│      
├─img                               保存程序运行中的全部图片资源
│      cache_0.png
│      
├─robotUI                         设计UI文件夹
│  │  main.py                     UI主函数
│  │  ui.ui                           UI界面
│  │  Ui_ui.py                     自动编译生成文件
│  │  
│  ├─drawedImg
│  │      source_img.png
│  │      
│  ├─icon                           主界面图标
│  │      icon.png
│  │      
│  ├─srcImg
│  │      source_img.png
│  │      
│  ├─ui_utils                      UI设计工具类源文件
│  │  │  imgCvt.py             图片转换函数
│  │  │  
│  │  └─__pycache__
│  │          imgCvt.cpython-36.pyc
│  │          
│  └─__pycache__
│          Ui_ui.cpython-36.pyc
│          
├─src                               存放后端主程序源文件
│  │  painter.py                   实现画图、操作栈维护等操作
│  │  __init__.py
│  │  
│  └─__pycache__
│          painter.cpython-36.pyc
│          __init__.cpython-36.pyc
│          
└─utils                             存放工具类源文件
    │  operation_stack.py          提供操作栈类
    │  __init__.py
    │  
    └─__pycache__
            operation_stack.cpython-36.pyc
            __init__.cpython-36.pyc
```

## 第一版

### UI界面

![UI界面](/githubImg/UI.jpg "UI")

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
- 字符：字体大小、线条宽度、首字符左下角x坐标、首字符左下角y坐标，字符内容、颜色

### 更新记录

- 2021/8/18 实现了直线、矩形、圆的绘制函数
- 2021/8/18 实现简答UI界面，并实现显示图片功能
- 2021/8/19 实现了操作记录的保存功能，提供操作的撤销及恢复功能
- 2021/8/19 优化UI界面，实现画直线、矩形、圆、椭圆、字符串功能界面。实现前三个画图功能
- 2021/8/19 修改了操作栈的存储逻辑，直接对Mat对象进行存储
- 2021/8/19 实现了椭圆和字符的绘制功能
- 2021/8/19 实现了UI画椭圆、字符功能，以及保存按钮功能