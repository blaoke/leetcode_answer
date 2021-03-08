#自顶向下解决
# class Solution:
#     def integerBreak(self, n: int) -> int:
#         if n < 2:
#             return 1
#         memo=[-1 for _ in range(n+1)]#存储n+1个值的最大值
#
#         def breakint(n:int):#将n进行分割
#             res = -1
#             if n<2:
#                 return 1
#             if memo[n]!=-1:
#                 return memo[n]
#             for i in range(1, n):  # 从1到n-1,
#                 res=max(res,i*(n-i),i*breakint(n-i))#res是当前结果和另外两部分求最大值
#             memo[n]=res
#             return res
#         breakint(n)
#         print(breakint(n))
# a=Solution()
# a.integerBreak(n=10)

#动态规划解决
class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 3:
            return 1
        memo=[1 for _ in range(n+1)]#存储每一个n+1个值至少分割2次后的最大值
        for i in range(3,n+1):
            for j in range(1,i):
              memo[i] =max(memo[i],j*(i-j),j*memo[i-j])#求一次拆分,和多次拆分的最大值
        return memo[n]
a=Solution()
print(a.integerBreak(n=4))

