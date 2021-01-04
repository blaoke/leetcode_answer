# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
#[31,26,33,21,40]
import random
class Solution:
    def lastStoneWeightII(self, stones: [int]) -> int:
        while(len(stones)>1):
            a=len(stones)
            i,j=random.randint(0,a)
            if stones[i]==stones[j]:

            else:
                stones[-1]=stones[-1]-stones[-2]
                stones.pop(-2)

                未完成

