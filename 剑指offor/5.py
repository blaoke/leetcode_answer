#常规方法
class Solution:
    def replaceSpace(self, s: str) -> str:
        s.split(' ')
        res = ''
        for i in s.split(' '):
            res += i + '%20'
        return res[:-3]
#一般方法
class Solution:
    def replaceSpace(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)) :
            if s[i] == ' ':
                s[i] = '%20'
        return ''.join(s)
