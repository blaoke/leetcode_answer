class Solution:
    def intersect(self, nums1:[int], nums2: [int]):
        ln1=len(nums1)
        ln2=len(nums2)
        a={}
        b=[]
        for i in range(ln1):
            if nums1[i] not in a.keys():
                a[nums1[i]]=1
            else:
                a[nums1[i]]+=1
        for i in range(ln2):
            if nums2[i] in a.keys() and a[nums2[i]]!=0:
                a[nums2[i]]-=1
                b.append(nums2[i])
        print(b)

aa=Solution()
aa.intersect(nums2 = [4,9,5], nums1 = [9,4,9,8,4])
