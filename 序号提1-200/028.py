# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        c=-1
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                c=i
                break
        # return c
        print(c)
a=Solution()
a.strStr(haystack='aaa',needle='a')

