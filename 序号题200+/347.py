#方法一
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        a={}
        res=[]
        heap=[]#构建堆
        lens=len(nums)
        # 下面for语句构造哈希表可以用这个语句代替 a=Counter(nums)
        for i in range(lens):
            if nums[i] not in a:
                a[nums[i]]=1
            else:
                a[nums[i]]+=1
        for key,value in a.items():
            heapq.heappush(heap,[-value,key])#heapq默认是小根堆,-value表示成大根堆
        for i in range(k):
            res.append(heapq.heappop(heap)[1])#heapq.heappop(heap)[1]表示是heap的key位置值
        print(res)


a=Solution()
a.topKFrequent(nums=[1,2,2,1,3,1],k=2)


#方法二
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.values())
