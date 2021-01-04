class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2: #如果seack2不为空,直接弹出栈顶元素
            return self.stack2.pop()
        else:
            while self.stack1:
                top=self.stack1.pop()
                self.stack2.append(top)
            return self.stack2.pop() if self.stack2 else -1


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2: 
            return self.stack2[-1]
        else:
            while self.stack1:
                top=self.stack1.pop()
                self.stack2.append(top)
            return self.stack2[-1] if self.stack2 else -1


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        while self.stack1:
                top=self.stack1.pop()
                self.stack2.append(top)
        return len(self.stack2)==0