# !/usr/stonesin/env/ python
# -*- coding:utf-8 -*-
class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        while(len(stones)>1):
            stones.sort()
            if stones[-1]==stones[-2]:
                stones.pop(-1)
                stones.pop(-1)
            else:
                stones[-1]=stones[-1]-stones[-2]
                stones.pop(-2)
        if stones:
            print(stones[0])
        else:
            print(0)

a=Solution()
a.lastStoneWeight(stones=[2,7,4,1,8,1])