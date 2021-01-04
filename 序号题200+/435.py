#使用贪心算法,先将所有的区间进行从小到大的排序,之后选择相同起点下结尾更小的区间,这样的区间留给后面的空间更大
class Solution:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        n=len(intervals)
        if n==0:
            return 0
        intervals.sort(key=lambda x: x[1])#将intervals按照末尾按照从小到大进行排序
        res=1   #保存的是最长的没有重叠的区间个数
        pre=0   #pre为结束最早的区间对应的索引
        for i in range(1,n):
            if intervals[i][0]>=intervals[pre][1]:
                res+=1
                pre=i
        return n-res
