#这道题没什么意思
from collections import deque #引入双端队列
class MaxQueue:
    def __init__(self):
        self.queue=deque([])
        self.deque=deque([])
    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1]<=value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        res=self.queue.popleft()
        if res==self.deque[0]:
            self.deque.popleft()
        return res