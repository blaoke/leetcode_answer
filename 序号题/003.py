#双指针解决,固定做指针,移动右指针,将遇到元素存入集合,如果遇到重复元素,就移动左指针,并删除集合中元素,直到无重复元素,继续移动右指针
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls=[0]*256
        lens=0
        l=0
        r=-1
        while l<len(s):
            if r+1<len(s) and ls[ord(s[r+1])]==0 :
                r+=1
                ls[ord(s[r])]+=1
            else:
                ls[ord(s[l])]=0
                l+=1
            lens=max(lens,r-l+1)
        print(lens)


a=Solution()
a.lengthOfLongestSubstring(s="pwwkew")

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = set()
        lens = 0
        l = 0
        r = -1
        while l<len(s):
            if r+1<len(s) and s[r+1] not in ls:
                r+=1
                ls.add(s[r])
            else:
                ls.remove(s[l])
                l+=1
            lens=max(lens,r-l+1)
        print(lens)
a=Solution()
a.lengthOfLongestSubstring(s="pwwkew")