class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if len(p)>=2 and p[1]=='*': #考虑第二个为'*'的情况
            if self.isMatch(s,p[2:]):  #'abc' 'a*abc'/'b*abc'
                return True
            if s and p[0]=='.': #如果pattern[0]为'.'的情况
                return self.isMatch(s[1:],p)
            if  s and s[0]==p[0]: #'*'表示匹配一次,如果pattern[0]与str[0]匹配,s向后,p不变:表示两层意思(1.将下一次的''
                return self.isMatch(s[1:],p)

        else:
            if s and (s[0]==p[0] or p[0]=='.'):
                return self.isMatch(s[1:],p[1:])
        return False

a=Solution()
print(a.isMatch(s = "ab", p =".*c"))