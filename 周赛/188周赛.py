# class Solution:
#     def buildArray(self, target: [int], n: int) :
#         stack=[]
#         lists=[_ for _ in range(1,n+1)]
#         res=[]
#         i=0
#         while stack!=target:
#             top=lists.pop(0)
#             stack.append(top)
#             res.append('push')
#             if stack[-1]==target[i]:
#                 i+=1
#             else:
#                 stack.pop()
#                 res.append('pop')
#         return res
#
# a=Solution()
# print(a.buildArray(target=[1,3],n=3))

# class Solution:
#     def countTriplets(self, arr: [int]) -> int:
#         n=len(arr)
#         res=0
#         for i in range(n-1):
#             for j in range(i+1,n):
#                 a=0 #0与任何数异或都为那个数本身
#                 for i1 in range(i,j):
#                     a=arr[i1]^a
#                 b=0
#                 for j1 in range(j,n):
#                     b=arr[j1]^b
#                     if b==a:
#                         res+=1
#         return res
#1443题
#方法一:使用深度优先搜索
import collections
class Solution:
    def minTime(self, n: int, edges: [[int]], hasApple: [bool]) -> int:
        build_tree=collections.defaultdict(list) #构造的树
        for i,j in edges:
            build_tree[i].append(j)
        def dfs(root):
            ret=0
            if  root in build_tree:
                for child in build_tree[root]:
                    tmp=dfs(child) #每个子节点得到的距离
                    if hasApple[child]==True or tmp!=0: #如果当前节点的子节点为苹果或者这个子节点的子节点是苹果,那么当前节点就要纳入计算
                        ret+=2
                    ret+=tmp
            return ret
        return dfs(0)
a=Solution()
print(a.minTime(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [False,False,True,False,True,True,False]))

#方法二,将每一个从根节点到苹果节点的所有路径存入集合(集合有去重作用),最后返回2*所有路径长度
class Solution:
    def minTime(self, n: int, edges: [[int]], hasApple: [bool]) -> int:
        apple_tree={}
        for i in edges:
            apple_tree[i[1]]=i[0]
        res=set() #存储路径的集合
        for j in hasApple:
            if j:
                heads=j
                while heads!=0: #如果当前节点没有到达根节点
                    res.add((apple_tree[heads],heads))
        return len(res)*2



