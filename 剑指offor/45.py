#本题实质上是一道排序题,只是需要自己定义排序规则,如果m*n<n*m -> m<n,如果m*n=n*m -> m=n
#其他的套用快排模板即可
class Solution:
    def minNumber(self, nums: [int]) -> str:
        n = len(nums)
        if n < 2:
            return str(nums[0])
        def quick_sort(nums, left, right):
            if left > right:
                return
            i, j = left, right
            while i != j:
                while int(nums[left] + nums[j]) <= int(nums[j] + nums[left]) and i < j:  # 即mn<nm说明m<n
                    j -= 1
                while int(nums[left] + nums[i]) >= int(nums[i] + nums[left]) and i < j:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[left], nums[i] = nums[i], nums[left]
            quick_sort(nums, left, i - 1)
            quick_sort(nums, i + 1, right)
        nums = [str(i) for i in nums]
        quick_sort(nums, 0, n - 1)
        return ''.join(nums)
a=Solution()
print(a.minNumber(nums=[2,56,4,20]))

