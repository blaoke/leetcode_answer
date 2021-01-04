#利用集合解决问题,easy
class Solution:
    def intersection(self, nums1: [int], nums2: [int]) :
        num1=set(nums1)
        num2=list(set(nums2))
        res=[]
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                res.append(nums2[i])
        print(list(set(res)))

a=Solution()
a.intersection(nums1 = [1,2,2,1], nums2 = [2,2])