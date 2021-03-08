#建立集合a,并保持集合的长度为k+1,当长度超过k+1时,删除i-k的元素
class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        a=set()
        for i in range(len(nums)):
            if nums[i]  in a:
                return True
            a.add(nums[i])
            if len(a)>k:
                a.remove(nums[i-k])

        return False


a=Solution()
# a.containsNearbyDuplicate(nums = [1,2,3,1], k = 3)
a.containsNearbyDuplicate(nums = [1,0,1,1], k = 1)

#方法二:利用字典,键为每个元素的值,对应的值为索引,如果在字典中就判断索引与当前值的距离是否<=k
class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        a={}
        for i in range(len(nums)):
            if nums[i] in a and i-a[nums[i]]<=k:
                return True
            a[nums[i]]=i
        return False

a=Solution()
a.containsNearbyDuplicate(nums = [1,2,3,1], k = 3)