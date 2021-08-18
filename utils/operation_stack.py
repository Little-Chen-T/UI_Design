class OperationStack():

    """操作堆栈，实现操作的恢复与撤销"""

    def __init__(self, init_img="cache_0"):

        self.__stack = ["img/"+init_img+".png"]
        self.__order = int(init_img.split("_")[1])
        self.__front = 0

    def push(self):
        
        """将操作记录压入操作栈"""

        self.__order += 1
        img_name = "img/cache_" + str(self.__order) + ".png"
        
        if len(self.__stack) == self.__front + 1:
            self.__stack.append(img_name)
            self.__front += 1
        else:
            self.__front += 1
            self.__stack[self.__front] = img_name

    def rollback(self):

        """撤销操作"""

        if (self.__front >= 1):
            self.__fornt -= 1
        else:
            ...

    def recover(self):

        """恢复操作"""

        if (self.__front == len(self.__stack) - 1):
            ...
        else:
            self.__front += 1
            history = self.__stack[self.__fornt-1].split("_")[1]
            new = self.__stack[self.__front].split("_")[1]
            if new < history:
                self.__front -= 1

    def front(self):

        """访问栈顶操作"""

        return self.__stack[self.__front]       