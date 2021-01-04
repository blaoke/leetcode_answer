#方法一:
# 与主站第3题相同,遍历双指针移动,如果右指针指向为区间中元素,就移动左指针,直到区间中不包含右指针指向元素为止
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        ls = set()
        lens = 0
        l = 0
        r = 0
        while l<len(s):
            if r<len(s) and s[r] not in ls:
                ls.add(s[r])
                r+=1
            else:
                ls.remove(s[l])
                l+=1
            lens=max(lens,r-l)
        return lens
a=Solution()
print(a.lengthOfLongestSubstring(s='abcabcbb'))

#方法二:在方法一的基础上进行优化,方法一如果在区间内有重复元素,就需要不断移动左指针,直到区间内无重复元素,这样的时间复杂度超过o(n),
#方法二是在方法一的基础上,除记录遍历的元素外还用字典记录这个元素在最后一次出现的下标,当有重复元素出现时 更新 左指针的值 和 这个重复元素在字典中下标
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        ls = {}
        lens = 0
        l = 0
        for r in range(n):
            if  s[r] not in ls:
                ls[s[r]]=r
            else:
                l=max(ls[s[r]]+1,l) #左指针为这个重复元素上一次出现的位置+1和当前左指针位置的最大值(因为重复元素上一次出现的位置可能不在当前遍历的区间内,所以不用管)
                ls[s[r]]=r #更新这个重复元素最后一次出现的下标
            lens=max(lens,r-l+1)
        return lens
a=Solution()
print(a.lengthOfLongestSubstring(s='abcabcbb'))