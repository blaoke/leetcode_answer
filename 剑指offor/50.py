import collections
class Solution:
    def firstUniqChar(self, s: str) -> str:
        s=list(s)
        n = len(s)
        if n == 0:
            return ' '
        dic=collections.Counter(s)
        for i in s:
            if dic[i]==1:
                return i
        return ' '
a=Solution()
print(a.firstUniqChar(s="loveleetcode"))

