#5424
# class Solution:
#     def maxProduct(self, nums: [int]) -> int:
#         maxs=max(nums)
#         index=nums.index(maxs)
#         n=len(nums)
#         ret=float('-inf')
#         for i in range(n):
#             if i != index:
#                 tmp=(maxs-1)*(nums[i]-1)
#                 if tmp>ret:
#                     ret=tmp
#         return ret
# a=Solution()
# print(a.maxProduct(nums=[1,5,4,5]))

#5425
# class Solution:
#     def maxArea(self, h: int, w: int, horizontalCuts: list, verticalCuts: list) -> int:
#         horizontalCuts.sort()
#         verticalCuts.sort()
#         hl=0
#         h_max=0
#         for item in horizontalCuts:
#             h_max=max(h_max,item-hl)
#             hl=item
#         if h-hl>h_max:
#             h_max=h-hl
#         wl=0
#         w_max=0
#         for j in verticalCuts:
#             w_max=max(w_max,j-wl)
#             wl=j
#         if w-wl>w_max:
#             w_max=w-wl
#         return (h_max*w_max)%(10**9+7)
# a=Solution()
# print(a.maxArea(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]))

# class Solution:
#     def minReorder(self, n: int, connections: [[int]]) -> int:
#         length=n-1 #路的总数
#         road={0}
#         connections.sort(key=lambda x:x[0])
#         ret=0
#         for i in range(length):
#             start=connections[i][0]
#             end=connections[i][1]
#             if start in road:
#                 road.add(end)
#             else:
#                 if end in road:
#                     road.add(start)
#                     ret+=1
#         return length-ret
#
# a=Solution()
# print(a.minReorder(n = 3, connections = [[1,0],[2,0]]))
import collections
class Solution:
    def getProbability(self, balls: [int]) -> float:
        sums_ball=sum(balls)
        tou=1
        for i in range(1,sums_ball+1):
            tou=tou*i
        mu=1
        for item in balls:
            if item!=1:
                mu=mu*item
        total=tou/mu

        dic=collections.Counter(balls)







        