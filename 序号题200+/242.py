class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic=dict()
        for i in s:
            if i not in dic:
                dic.setdefault(i,1)
            else:
                dic[i]+=1
        for j in t:

            if j not in dic:
                return False
            if dic[j]>0:
                dic[j]-=1

            if dic[j] == 0:
                dic.pop(j)
        if not dic:
            return True
        else:
            return False

a=Solution()
print( a.isAnagram(s = "rat", t = "car"))