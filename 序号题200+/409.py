import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        a=collections.Counter(s)
        maxodd=0
        ret=0
        for i in a:
            if a[i]%2==0:
                ret+=a[i]
            else: #表示奇数存在
                ret+=a[i]-1 #加上比这个奇数小一的偶数
                maxodd=1 # 就需要除加上比它小一的偶数外还要加1
        ret+=maxodd
        return ret

a=Solution()
a.longestPalindrome(s="ccc")
