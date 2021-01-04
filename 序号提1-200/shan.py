
# a={1:2,3:5,8:7}
# res=filter(lambda x:x%2!=0,a.values())
# print(len(res))
# c=[[2,3],[4,0],[0,1],[1,3],[4,5]]
# c.sort(key=lambda x:x[0])
# print(c)
import collections
ball=[2,2,1,1]
dic=collections.Counter(ball)
print(dic)