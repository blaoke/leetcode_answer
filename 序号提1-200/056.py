#方法:使用双指针,i和j
class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        intervals.sort(key=lambda x:x[0]) #按照数组的第一个值排序
        n=len(intervals)
        res=[]
        i=0
        while i <n:
            right=intervals[i][1] #定义数组的右边值
            j=i+1
            while j<n and right>=intervals[j][0]:
                right=max(right,intervals[j][1]) #更新右边值为最大值
                j+=1
            res.append([intervals[i][0],right])  #直到没有重叠元素,添加
            i=j
        return res