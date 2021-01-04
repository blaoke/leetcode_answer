class Solution:
    def validPalindrome(self, s: str) -> bool:
        target=0
        n=len(s)
        l,r=0,n-1
        while l+1<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                if target==1:
                    return False
                elif target==0:
                    if s[l + 1] == s[r] and s[l + 2] == s[r - 1]: #这个地方测试用例有点鸡贼,所以要两次确认
                        l += 2
                        r -= 1
                        target += 1
                    elif s[l] == s[r - 1] and s[l+1]==s[r-2]:
                        r -= 2
                        l += 1
                        target += 1
                    else:
                        return False
        return True

a=Solution()
print(a.validPalindrome(s='"ebcbbececabbacecbbcbe"'))

class Solution(object):
    def validPalindrome(self, s):
        def inv(s):
            return s==s[::-1] #是否是回文子串
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return inv(s[left+1:right+1]) or inv(s[left:right]) #判断left+1到right 或者 left到right-1 是不是回文子串
        return True
