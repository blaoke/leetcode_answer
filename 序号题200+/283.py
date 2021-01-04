#时间复杂度 o(n) 空间复杂度o(1)
#方法一
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k=0
        n=len(nums)
        for i in range(n):
            if nums[i]:
                nums[k]=nums[i]
                k+=1
        for j in range(k,n):
            nums[j]=0
        return nums
            
           
#方法二 在方法一的基础上，利用非零元素与零元素交换位置
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k=0
        n=len(nums)
        for i in range(n):
            if nums[i]:
                nums[k],nums[i]=nums[i],nums[k]
                k+=1
        return nums
