class Solution:
    def containsNearbyAlmostDuplicate(self, nums: [int], k: int, t: int) -> bool:
        a=set()
        s=0
        if not nums:
            return False
        for i in range(len(nums)):
            if len(a)>k:
                a.remove(nums[i-(k+1)])
            # if a :
            if t==0:
                if nums[i] in a:
                    return True
            else:
                for j in a:
                    if abs(nums[i]-j)<=t :
                        # return True
                        s=1
            a.add(nums[i])
        # return False
        print(s)

a=Solution()
# a.containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3)  #false
# a.containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0)   #true
# a.containsNearbyAlmostDuplicate(nums = [1,0,1,1], k = 1, t = 2)  #ture
a.containsNearbyAlmostDuplicate(nums = [1,2], k = 0, t = 1)  #false
# a.containsNearbyAlmostDuplicate(nums = [7,2,8], k = 2, t = 1)  #true

# a.containsNearbyAlmostDuplicate(nums = [4,1,6,3], k = 100, t = 1)  #true

#桶方法
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or k < 0:
            return False
        all_buckets = {}
        bucket_size = t + 1  # 桶的大小设成t+1更加方便
        for i in range(len(nums)):
            bucket_num = nums[i] // bucket_size  # 放入哪个桶

            if bucket_num in all_buckets:  # 桶中已经有元素了
                return True

            all_buckets[bucket_num] = nums[i]  # 把nums[i]放入桶中

            if (bucket_num - 1) in all_buckets and abs(all_buckets[bucket_num - 1] - nums[i]) <= t:  # 检查前一个桶
                return True

            if (bucket_num + 1) in all_buckets and abs(all_buckets[bucket_num + 1] - nums[i]) <= t:  # 检查后一个桶
                return True

            # 如果不构成返回条件，那么当i >= k 的时候就要删除旧桶了，以维持桶中的元素索引跟下一个i+1索引只差不超过k
            if i >= k:
                all_buckets.pop(nums[i - k] // bucket_size)

        return False

a = Solution()
a.containsNearbyAlmostDuplicate(nums = [1,2,3,1], k = 3, t = 0)   #true

