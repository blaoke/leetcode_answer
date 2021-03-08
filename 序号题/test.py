# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
class Solution:
    def robot(self, command: str, obstacles: [[int]], x: int, y: int) -> bool:
        i=0;j=0
        dic={'u':j+1,'r':i+1}
        while(i<=x or j<=y):
            for _ in range(len(command)):
                dic.get(command[_])
                if i==obstacles[0][0] and j==obstacles[0][1]:
                    return False
                    break
        return True
a=Solution()
a.robot(command = "URR", obstacles = [[4, 2]], x = 3, y = 2)
