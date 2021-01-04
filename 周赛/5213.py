# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
class Solution:
    def minCostToMoveChips(self, chips: [int]) -> int:
        chips=sorted(chips)
        b = [0] * 3
        for i in range(len(chips)):
            if chips[i]%2==0:
                b[2] += 1
            else:
                b[1]+=1
        print(min(b[1],b[2]))
a=Solution()
a.minCostToMoveChips(chips=[3,3,1,2,2])
