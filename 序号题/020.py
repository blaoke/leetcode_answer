# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
# 方法：用栈的方法，如果是左括号就入栈，如果有右括号就和栈顶元素匹配，两者符合就出栈，不符合返回false
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={')':'(','}':'{',']':'['}
        for i in s:
            if i in mapping:
                top=stack.pop() if stack else '@'
                if mapping[i]!=top:
                    return False
                    break
            else:
                stack.append(i)
        return not stack
a=Solution()
a.isValid(s='}')

