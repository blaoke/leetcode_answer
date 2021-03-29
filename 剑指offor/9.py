#利用两个栈,入队的时候将元素都压入stack1,如果要出队列,就将stack1的所有元素都出栈再入栈到stack2,这样stack2的栈顶元素就是最先如入队的元素,
# 如果再要入队,就将元素压到stack1,出队时只有在stack2栈为空时，才将stack1中元素压入、
#入队直接加入stack1,出队的话首先看stack2中是否有元素，如果有则直接出栈，如果stack2为空，则将stack1中元素全部放入stack2,然后从stack2出栈
class CQueue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack2: #如果seack2不为空,直接弹出栈顶元素
            return self.stack2.pop()
        else: #如果stack2为空
            while self.stack1: #将stack1中元素压入stack2,如果有的话
                top=self.stack1.pop()
                self.stack2.append(top)
            return self.stack2.pop() if self.stack2 else -1 #如果stack2没元素就返回-1