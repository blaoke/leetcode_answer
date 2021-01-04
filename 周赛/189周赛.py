# #5412
# class Solution:
#     def busyStudent(self, startTime: [int], endTime: [int], queryTime: int) -> int:
#         n=len(startTime)
#         res=0
#         for i in range(n):
#             if startTime[i]<=queryTime and endTime[i]>=queryTime:
#                 res+=1
#         return res

#5413
# class Solution:
#     def arrangeWords(self, text: str) -> str:
#         text=text.lower()
#         b=text.split(' ')
#         c=sorted(b,key=lambda x:len(x))
#         res=' '.join(c).capitalize()
#         return res

#5414
# class Solution:
#     def peopleIndexes(self, favoriteCompanies: [[str]]) -> [int]:
#         res=[]
#         n=len(favoriteCompanies)
#         b=sorted(enumerate(map(set,favoriteCompanies)),key=lambda x:len(x[1]),reverse=True)
#         for i in range(n):
#             new=False
#             for j in range(i):
#                 if b[i][1].issubset(b[j][1]): #如果当前数组是前面遍历数组的子集,就直接返回
#                     new=True
#                     break
#             if new==False:
#                 res.append(b[i][0])
#         res.sort()
#         return res
# a=Solution()
# print(a.peopleIndexes(favoriteCompanies=[["google","microsoft"],["leetcode","google","facebook"],["google","facebook"],["google"],["amazon"]]))

#5415
# import math
# class Solution:
#     def numPoints(self, p: List[List[int]], r: int) -> int:
#         res = 1
#
#         def dis(pi, pj):
#             return math.sqrt((pi[0] - pj[0]) ** 2 + (pi[1] - pj[1]) ** 2)
#
#         def center(pi, pj):
#             mid = ((pi[0] + pj[0]) / 2, (pi[1] + pj[1]) / 2)
#
#             angle = math.atan2(pi[0] - pj[0], pj[1] - pi[1])
#             # print(pi, pj)
#             d = math.sqrt(r ** 2 - dis(pi, mid) ** 2)
#             return (mid[0] + d * math.cos(angle), mid[1] + d * math.sin(angle))
#         n = len(p)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if dis(p[i], p[j]) > r * 2:
#                     continue
#                 c = center(p[i], p[j])
#                 cur = 0
#                 for k in range(n):
#                     if dis(c, p[k]) <= r + 10 ** (-7):
#                         cur += 1
#                 res = max(res, cur)
#         return res
