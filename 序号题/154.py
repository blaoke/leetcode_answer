class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        if nums[left] < nums[right]:
            return nums[0]
        mid = (left + right) // 2
        while right - left > 1:
            if nums[mid] == nums[left] == nums[right]:  # 在遇到[10,1,10,10,10] 这种情况时,只能从前往后遍历
                mins = nums[left]
                for i in range(left + 1, right):
                    if nums[i] < mins:
                        mins = nums[i]
                return mins

            if nums[mid] >= nums[left]:
                left = mid
            else:
                right = mid
            mid = (left + right) // 2
        return nums[right]