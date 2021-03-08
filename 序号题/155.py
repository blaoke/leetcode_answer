#方法:建立一个栈和一个存储最小值的辅助栈,每次除向栈中压入元素外,还要比较辅助栈的栈顶元素与当前压入值的大小,将两者中的较小值压入辅助栈
#当弹出栈时,同时弹出栈和辅助栈的栈顶元素
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[] #栈
        self.stack_min=[] #存储最小值的辅助栈

    def push(self, x: int) -> None:
        if not self.stack_min:
            self.stack_min.append(x)
        else:
            mins =min( self.stack_min[-1],x)
            self.stack_min.append(mins)
        self.stack.append(x)
    def pop(self) -> None:
        self.stack_min.pop()
        return self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.stack_min[-1]
