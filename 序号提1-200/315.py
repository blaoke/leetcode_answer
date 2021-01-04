#方法一:将nums中的每个元素从后向前插入到一个递增的有序数组中,插入到数组中的位置就是这个元素在nums中后面比它小的元素个数
#使用python中 bisect 方法:
#bisect.insort(list,num) 将num数字插入到有序数组list中
#bisect.bisect(list,num)返回将num插入到list中的位置索引
#bisect.bisect_left(list,num) 和 bisect_right 函数处理插入的num在list中存在时,返回插入到已经存在的元素左边还是右边的索引
#bisect.insort_left 和 insort_right处理插入的情况(同上)
import bisect
class Solution:
    def countSmaller(self, nums: [int]) :
        sortns = []
        res = []
        nums.reverse()
        for n in nums:
            idx = bisect.bisect_left(sortns, n) #在排序的sortns数组中确定插入n的位置索引
            res.append(idx)
            bisect.insort(sortns,n)
        return res[::-1]


class treeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.count = 0


class Solution:
    def countSmaller(self, nums):
        len_nums = len(nums)
        if len_nums == 0:
            return []

        root = treeNode(nums[len_nums - 1])
        res = [0 for _ in range(len_nums)]
        for i in reversed(range(0, len_nums - 1)):
            newNode = treeNode(nums[i])
            node = root
            while True:
                if newNode.val > node.val:
                    res[i] += node.count + 1
                    if node.right != None:
                        node = node.right
                    else:
                        node.right = newNode
                        break
                else:
                    node.count += 1
                    if node.left != None:
                        node = node.left
                    else:
                        node.left = newNode
                        break

        return res


