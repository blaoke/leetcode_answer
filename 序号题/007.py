# !/usr/bin/env/ python
# -*- coding:utf-8 -*-
# class Solution:
#     def reverse(self, x: int) -> int:
#         res,fu=0,1
#         if x<0:
#             fu=-1
#             x=-1*x
#         while x!=0:
#             res=res*10+x%10
#             if res>2147483647:
#                 return 0
#             x=int(x/10)
#         print(res*fu)
# a=Solution()
# a.reverse(x=-123)

'"--------------- "'
class Solution(object):
    def reverse(self, x:int):
        res_stack=[]
        a=1
        if x<0:
            a=-1
            x=x*a
        b=list(str(x))
        while b:
            v = b.pop()
            res_stack.append(v)
        c=int("".join(res_stack))
        if c > 2147483647:
            return 0
        res = c * a
        print(res)
        #return res
a=Solution()
a.reverse(x=-788900)