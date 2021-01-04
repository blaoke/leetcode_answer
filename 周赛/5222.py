# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
# a={'R':'L','L':'R'}
# s="RLRRLLRLRL"
# b=[]

# for i in range(len(s)):
#     item=s[i]
#     tar=a[item]
#     if len(b)==0:
#         b.append(item)
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        a = {'R': 1, 'L': -1}
        sus = 0
        all = 0
        for i in range(len(s)):
            item = s[i]
            sus += a[item]
            if sus == 0:
                all += 1
        return all
a=Solution()
a.balancedStringSplit(s="RLLLLRRRLR")




