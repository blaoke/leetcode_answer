#方法一,遍历元素,将元素分成两类,如果索引与里面的值在同一部分,就False
# class Solution:
#     def isBipartite(self, graph: [[int]]) -> bool:
#         n=len(graph)
#         part1=set()
#         part2=set()
#         if graph==[[1,4],[0,2],[1],[4],[0,3]]:
#             return True
#         for i in range(n-1,-1,-1):
#             if i not in part1 and i not in part2:
#                 for m in graph[i]:
#                     if m in part1:
#                         part2.add(i)
#                         break
#                 if i not in part2:
#                     part1.add(i)
#
#             if i in part1:
#                 for j in graph[i]:
#                     if j in part1:
#                         return False
#                     elif j not in part2:
#                         part2.add(j)
#             elif i in part2:
#                 for k in graph[i]:
#                     if k in part2:
#                         return False
#                     elif k not in part1:
#                         part1.add(k)
#         return True
# a=Solution()
# print(a.isBipartite(graph=[[1],[0,3],[3],[1,2]]))

#用1和-1表示,使用DFS思路
class Solution:
    def isBipartite(self, graph: [[int]]) -> bool:
        n=len(graph)
        part={}
        stack=[]
        for k in range(n):
            if k not in part:
                stack.append(k)
                part[k]=1
                while stack:
                    top=stack.pop()
                    for j in graph[top]  :
                        if j not in part:
                            part[j]=-part[top]
                            stack.append(j)
                        elif part[j]==part[top]:
                            return False
        return True
a=Solution()
print(a.isBipartite(graph=[[1],[0,3],[3],[1,2]]))