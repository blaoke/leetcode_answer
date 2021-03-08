#方法:开辟一个[0-最大天数]的数组,数组中的值等于min(前一天的值+2,前7天的值+7,前30天的值+15),不断更新,直到最后到达days数组的最后一天
class Solution:
    def mincostTickets(self, days: [int], costs: [int]) -> int:
        last_day=days[-1]
        months=[0 for _ in range(last_day+1)]
        j=0
        for i in range(1,last_day+1):
            if i!=days[j]:
                months[i]=months[i-1]
            else:
                months[i]=min(months[max(i-1,0)]+costs[0],months[max(0,i-7)]+costs[1],months[max(0,i-30)]+costs[2])
                j+=1
        return months[-1]
a=Solution()
print(a.mincostTickets(days =[1,4,6], costs = [7,2,15]))


