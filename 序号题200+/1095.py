#三次二分查找,第一次查找峰顶,第二次在峰顶左边查找,如果没查找到就在峰顶右边查找
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()-1
        l, r = 0, n 
        while l < r:
            mid = (r + l) // 2
            if mountain_arr.get(mid + 1) > mountain_arr.get(mid):
                l = mid + 1
            else:
                r = mid
        top = l

        def binary_search(mountain_arr, l, r, target,rise):
            while l <= r:
                mid = (l + r) // 2
                if mountain_arr.get(mid) == target:
                    return mid
                elif mountain_arr.get(mid) > target:
                    if rise==True: #判断是否在山峰的前面
                        r = mid - 1
                    else:
                        l=mid+1
                else:              #判断是否在山峰的前面
                    if rise==True:
                        l = mid + 1
                    else:
                        r=mid-1
            return -1

        index = binary_search(mountain_arr, 0, top, target,True)
        if index != -1:
            return index
        index = binary_search(mountain_arr*-1, top+1, n, target,False)
        return index

