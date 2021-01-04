#快速排序
class Solution:
    def sortArray(self, nums: [int]) :
        if len(nums)<2:
            return nums
        def quicksort(nums,left,right): #定义快排函数
            if left>right:
                return
            i=left
            j=right
            while i!=j:
                while nums[j]>=nums[left] and i<j:
                    j-=1
                while nums[i]<=nums[left] and i<j:
                    i+=1
                if i<j:
                    nums[i],nums[j]=nums[j],nums[i] #前后交换
            nums[left],nums[i]=nums[i],nums[left] #最后交换基准数和nums[i]的数值
            quicksort(nums,left,i-1)
            quicksort(nums,i+1,right)
        quicksort(nums,0,len(nums)-1)
        return nums
a=Solution()
print( a.sortArray(nums = [5,1,1,2,0,0]))


#归并排序,清晰写法
class Solution:

    def sortArray(self, nums: [int]) :
        self.merge_sort(nums)
        return nums

    def merge_sort(self, nums):
        if len(nums)<2:
            return nums
        #分
        mid=len(nums)//2
        left=self.merge_sort(nums[0:mid])
        right=self.merge_sort(nums[mid:])
        #合
        return self.merge(left,right)

    def merge(self, left, right):
        i = 0  # 左边指针
        j = 0  # 右边指针
        ret = []  # 存储的外用数组
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ret.append(left[i])
                i += 1
            else:
                ret.append(right[j])
                j += 1
        ret += left[i:]  # 如果左边数组还有没合并的就添加到后面
        ret += right[j:]  # 同理
        return ret






