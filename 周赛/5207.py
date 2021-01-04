# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def ordd(a:str,b:str):
            return abs(ord(a)-ord(b))
        def cha(a1:str,b1:str):#求两个字符串的ASCII的差值，组成一个列表c
            c=[]
            for i in range(len(a1)):
                c.append(ordd(a1[i],b1[i]))
            return c
        def chong(c: [], coat=maxCost):
            # b = [0 for i in range(len(c))]
            # for i in range(1, len(c)):
            #     if c[i] + c[i - 1] <= coat:
            #         b[i] += b[i - 1] + 1
            #         c[i] += c[i - 1]
            # if max(b)==0:  # 判断没有一个满足时的情况
            #     return max(b)
            # else:
            #     return max(b) + 1,b
            x = []
            for i in range(len(c) - 1):
                cc = [0]+c[i:len(c)]
                b = [0 for _ in range(len(cc))]
                # if cc[0]<=coat:
                #     b[0]=1
                for j in range(1, len(cc)):
                    if cc[j] + cc[j - 1] <= coat:
                        b[j] += b[j - 1] + 1
                        cc[j] += cc[j - 1]
                if max(b) == 0:  # 判断没有一个满足时的情况
                    x.append(max(b))
                else:
                    x.append(max(b))
            return max(x)
        print(chong(cha(s,t),coat=maxCost))
a = Solution()
a.equalSubstring(s="abcd", t="bcdf", maxCost=0)
# a.equalSubstring(s="ujteygggjwxnfl", t="nstsenrzttikoy", maxCost=43)
        # chong(a=[0, 1, 1, 1], coat=0)
        #
        # cost=0
        # for i in range(len(s)):
        #     if cost+ordd(s[i],t[i])<=maxCost:
        #         cost += ordd(s[i], t[i])
        #         a=i+1
        #     else:
        #         a=i
        #         break
        # print(a)

# def chong(a:[],coat=19):#
#     b=[0 for i in range(len(a))]
#     for i in range(1,len(a)):
#         if a[i]+a[i-1]<=coat:
#             b[i]+=b[i-1]+1
#             a[i]+=a[i-1]
#     print(max(b)+1,a)
# chong(a=[0,1,1,1],coat=0)

