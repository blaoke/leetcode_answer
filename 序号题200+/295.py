#同剑指offor41题
import heapq
class MedianFinder:
    def __init__(self):
        self.heap_max=[]
        self.heap_min=[]
        self.nums=0 #用于记录所有数的个数
    def addNum(self, num: int) -> None:
        if self.nums%2==0:#如果是偶数,就加入左边的大根堆
            if not self.heap_max:
                heapq.heappush(self.heap_max,-num)
            else:
                heap_min_top=self.heap_min[0]
                # heap_min_top=heapq.nsmallest(1,self.heap_min)[0] #求取最小堆中最小元素,
                if heap_min_top>=num: #如果要添加的元素小于最小堆的堆顶元素
                    heapq.heappush(self.heap_max,-num)
                else: #往最大堆中添加的元素大于最小堆的堆顶元素
                    heapq.heappush(self.heap_max,-heapq.heappop(self.heap_min))
                    heapq.heappush(self.heap_min,num)
        else:
            if not self.heap_min: #如果最小堆中无元素,就要向最小堆中添加元素
                heapq.heappush(self.heap_max,-num) #先向最大堆中添加元素,然后将最大堆中的最大元素添加到最小堆
                heapq.heappush(self.heap_min,-heapq.heappop(self.heap_max))
            else:
                heap_max_floor=-self.heap_max[0]
                # heap_max_floor=-heapq.nsmallest(1,self.heap_max)[0] #求取最大堆最大元素
                if heap_max_floor<=num:
                    heapq.heappush(self.heap_min,num)
                else:
                    heapq.heappush(self.heap_min,-heapq.heappop(self.heap_max))
                    heapq.heappush(self.heap_max,-num)
        self.nums += 1
    def findMedian(self) -> float:
        if self.nums%2==0:#数据流中元素个数为偶数
            return (-self.heap_max[0]+self.heap_min[0])/2
        else:
            return -self.heap_max[0]
