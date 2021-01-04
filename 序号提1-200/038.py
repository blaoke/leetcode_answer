# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.qiuhe(self.countAndSay(n-1))

    def qiuhe(self,c:str):
        a={'111':31,'222':32,'33':23,'22':22,'11':21,'1':11,'2':12,'3':13,'0':5}
        d=c+'00'
        n=[d]
        b=[]
        i=0
        while i <len(n[0])-2:
                if n[0][i]==n[0][i+1]:
                        if n[0][i+1]==n[0][i+2]:
                            b.append(a[n[0][i:i+3]])
                            i+=3
                        else:
                            b.append(a[n[0][i:i+2]])
                            i+=2
                else:
                    b.append(a[n[0][i]])
                    i+=1
        b=[str(i) for i in b]
        c=''.join(b)
        return c

a=Solution()
a.countAndSay(n=1)

#f方法二：方法一是在参考了方法2的递归实现实现的
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.bs(self.countAndSay(n - 1))

    def bs(self, string):
        lis = list(string)
        lis.append('0')  # 末尾补一个，方便后续计数
        lis1 = []
        re = 0
        i = 0
        while i < len(lis) - 1:
            if lis[i] != lis[i + 1]:
                lis1.append(str(i + 1 - re))  # 当前计录的值的个数
                lis1.append(lis[i])  # 当前记录的值
                re = i + 1
            i = i + 1
        s = ''.join(lis1)  # 列表转字符串
        return s
