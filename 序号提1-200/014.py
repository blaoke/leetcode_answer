# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
#方法一：利用zip(*)函数，将每一个单词的首字母组成集合，然后利用set()去重，最后依次判断
class Solution:
    def longestCommonPrefix(self, strs:[str]) -> str:
        a=zip(*strs)
        b=[]
        for i in a:
            if len(set(i))==0:
                break
            elif len(set(i))==1:
                b+=list(set(i))
            else:
                break
        print( str(''.join(b)) if b!=0 else " ")

s=Solution()
s.longestCommonPrefix(strs=["aca","cba"])
