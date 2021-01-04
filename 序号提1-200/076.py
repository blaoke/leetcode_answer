class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        cnt=collections.Counter(t)
        l=0
        n=0 #表示t中元素的种类
        ans=''
        for r,item in enumerate(s):
            if item not in cnt:
                continue
            cnt[item]-=1
            if cnt[item]==0:#在cnt中item总数刚好为需要的数目,即cnt[item]=0时,才让n加1
                n+=1
            while cnt[s[l]]<0 or s[l] not in cnt:#判断左边s[l]是或不是cnt元素,用于左窗口移动
                if s[l] in cnt:
                    cnt[s[l]]+=1
                l+=1
            if n==len(cnt) :#判断窗口包含t中每一种元素即可,有可能这个窗口中重复包含t中的元素,比要求的还要多,但是满足题意
                if not ans or len(ans)>r-l+1:#if  not ans用于给ans第一次赋值,
                    ans=s[l:r+1]
        print(ans)

a = Solution()
a.minWindow(s="aaaaaaaaaaaabbbbbcdd", t="abcdd")