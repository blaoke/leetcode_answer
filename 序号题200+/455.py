#最简单的贪心算法
#优先满足最贪心的小朋友
class Solution:
    def findContentChildren(self, g: [int], s: [int]) -> int:
        g.sort(reverse=-1)
        s.sort(reverse=-1)
        g1=0
        s1=0
        res=0
        while(g1<len(g) and s1<len(s)):
            if s[s1]>=g[g1]:
                res+=1
                s1+=1
                g1+=1
            else:
                g1+=1
        return res

#优先满足最不贪心小朋友
class Solution:
    def findContentChildren(self, g: [int], s: [int]) -> int:
        g.sort()
        s.sort()
        g1=0
        s1=0
        res=0
        while(g1<len(g) and s1<len(s)):
            if s[s1]>=g[g1]:
                res+=1
                s1+=1
                g1+=1
            else:
                s1+=1
        return res