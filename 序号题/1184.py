# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
class Solution:
    def distanceBetweenBusStops(self, distance: [int], start: int, destination: int) -> int:
        a=sum(distance)
        if destination<start:
            destination,start=start,destination
        sum1=sum(distance[start:destination])
        print(min(sum1,a-sum1))
b=Solution()
b.distanceBetweenBusStops(distance=[1,2,3,4],start=0,destination=3)