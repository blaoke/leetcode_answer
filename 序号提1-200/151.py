class Solution:
    def reverseWords(self, s: str) -> str:
        res=s.strip().split(' ')
        res=list(filter(lambda x:x!='',res))
        res.reverse()
        ret=' '.join(res)
        return ret

class Solution:
    def reverseWords(self, s: str) -> str:
        res=s.split()
        res.reverse()
        res=' '.join(res)
        return res

a=Solution()
print(a.reverseWords(s="a good   example"))