# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
class Solution:
    def checkStraightLine(self, coordinates: [[int]]) -> bool:
        a = coordinates[1][0] - coordinates[0][0]
        b = coordinates[1][1] - coordinates[0][1]
        i=True
        for x in range(2,len(coordinates)):
            if coordinates[x][0]==coordinates[x-1][0] or coordinates[x][1]==coordinates[x][1]:
                i=True
                break
            if ((coordinates[x][0] - coordinates[x - 1][0]) / (coordinates[x][1] - coordinates[x - 1][1])) != b / a:
                i = False
        print(i)

a=Solution()

a.checkStraightLine(coordinates =[[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]])



