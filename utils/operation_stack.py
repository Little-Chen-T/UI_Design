class OperationStack():

    """操作堆栈，实现操作的恢复与撤销"""

    def __init__(self, image):

        self.__stack = [image]
        self.__front = 0

    def push(self, image):
        
        """将操作记录压入操作栈"""
        
        if len(self.__stack) == self.__front + 1:
            self.__stack.append(image)
            self.__front += 1
        else:
            self.__front += 1
            self.__stack[self.__front] = image

    def rollback(self):

        """撤销操作"""

        if (self.__front >= 1):
            self.__front -= 1
        else:
            ...

    def recover(self):

        """恢复操作"""

        if (self.__front == len(self.__stack) - 1):
            ...
        else:
            self.__front += 1
            

    def front(self):

        """访问栈顶操作"""

        return self.__stack[self.__front]       