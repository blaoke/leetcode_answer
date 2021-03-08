#最开始想到的是双指针移动,可是由于数组中有负数,所以这种方法不能使用,而暴力方法超时,所以可以用前缀和法,用哈希表存储之前的所有前缀和结果
class Solution:
    def subarraySum(self, nums: [int], k: int) -> int:
        res=0
        sums=0
        dic={}
        for i in range(len(nums)):
            sums+=nums[i] #sums就表示前缀和
            if sums==k: #如果总和为k,结果就加1
                res+=1
            if sums-k in dic:  # 如果前缀和减去目标值k所得到的值在字典中出现，即当前位置前缀和减去之前某一位的前缀和等于目标值
                res+=dic[sums-k]
            if sums in dic: #如果这个前缀和在之前出现过,就在原来的基础上加一
                dic[sums]+=1
            else:
                dic[sums]=1 #如果没有出现过就在加入到哈希表中
        return res