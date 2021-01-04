# !/usr/bin/env/ python 
# -*- coding:utf-8 -*-
b=[]
c=[]
def yici(a: [int], b: [int], c: [int]):
    for i in range(len(a)):
        if a[i] == 0:
            b.append('out')
            break
        elif a[i] == 10:
            c.append('out')
        else:
            a[i] += 1
    return a, b, c
def onestep( a: [int], T: int):
    t = 0
    while t < T:
        yici(a, b, c)
        t = t + 1
        # a = list(filter(lambda x: x != 0 and x != 10, a))
    for i in range(len(a)):
        a[i] = abs(a[i])
    a.sort()
    print(b + a + c)

a=onestep(a=[1,-3,5,10],T=6)
