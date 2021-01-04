# 方法一：新建一个列表存放nums1[:m],时间复杂度o(n+m)
# def merge( nums1: [int], m: int, nums2: [int], n: int) -> None:
#     i=0
#     j=0
#     nums1_copy=nums1[:m]
#     nums1[:]=[]
#     while i <m and j <n:
#         if nums1_copy[i]<=nums2[j]:
#             nums1.append(nums1_copy[i])
#             i+=1
#         else:
#             nums1.append(nums2[j])
#             j+=1
#     if i<m:
#         nums1[i+j:]=nums1_copy[i:]
#     if j<n:
#         nums1[i+j:]=nums2[j:]
#     print(nums1)
# merge(nums1 = [1,2,3,0,0,0], m = 3,nums2 = [2,5,6],n=3)

# 方法二：尾插法,设置3个指针p1,p2,p,分别移动,将p1,p2中较大的一个赋值给P,然后不断向前移动
def merge( nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    # set pointer for nums1
    p = m + n - 1
    # while there are still elements to compare
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    # add missing elements from nums2
    nums1[:p2 + 1] = nums2[:p2 + 1]
    print(nums1)

merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)


