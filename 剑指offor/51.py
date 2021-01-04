#方法一:从后向前移动,使用filter函数挑选出已存元素中小于当前元素的元素,统计长度,将长度加入结果,这种方法的TC较高,为o(n*2)
class Solution:
    def reversePairs(self, nums: [int]) -> int:
        dic=[]
        res=0
        for i in range(len(nums)-1,-1,-1):
            if not dic:
                dic.append(nums[i])
            else:
                suit=list(filter(lambda x:x<nums[i],dic)) #挑选出已存元素中小于当前元素的元素
                lens=len(suit)  #统计长度
                dic.append(nums[i])
                res+=lens #将长度加入结果
        return res
a=Solution()
print( a.reversePairs(nums=[1,2,1,2,1]))

#方法二:先把数组分隔成子数组,统计出子数组内部的逆序对的数目,再统计出两个相邻子数组之间的逆序对数目,在统计逆序对的过程中需要对数组进行排序,
#是归并排序方法,因此算法的TC是O(nlogn),SC是O(n)
class Solution:
    def reversePairs(self, nums: [int]) -> int: