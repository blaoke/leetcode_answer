#同198题,方法二是方法一的改进版
class Solution:
    def massage(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        ret=[-1 for _ in range(n)]
        ret[0]=nums[0]
        for i in range(1,n):
            ret[i]=max(nums[i]+ret[i-2] if i-2>=0 else nums[i],ret[i-1])
        return ret[n-1]

class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        pre = cur = 0
        for i in range(n):
            cur, pre = max(nums[i] + pre, cur), cur
        return cur



