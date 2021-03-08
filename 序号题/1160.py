import collections
class Solution:
    def countCharacters(self, words: [str], chars: str) -> int:
        a=collections.Counter(chars) #这一句等同于下面一段的写法

        a = {}
        for item in chars:
            if item not in a:
                a[item] = 1
            else:
                a[item] += 1

        ret=0
        n = len(words)
        for i in range(n):
            s = 1
            b=a.copy() #字典a
            choice=words[i] #选择的单词
            for j in choice:
                if j in b and b[j]>0:
                    b[j]-=1
                else:
                    s=0
                    break
            if  s:
                ret+=len(words[i])
        return ret
a=Solution()
print(a.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))

class Solution:
    def countCharacters(self, words: [str], chars: str) -> int:
        ret=0
        for i in words:
            for j in i:
                if chars.count(j)<i.count(j):
                    break
            else:
                ret+=len(i)
        return ret