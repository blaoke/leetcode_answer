import heapq
class Solution:
    def getLeastNumbers(self, arr: [int], k: int) -> [int]:
        heap=[]
        if k==0:
            return heap
        for i in arr:
            if len(heap)<k:
                heapq.heappush(heap,-i)
            else:
                if heap[0]<-i:
                    heapq.heappop(heap)
                    heapq.heappush(heap,-i)
        return [-x for x in heap]