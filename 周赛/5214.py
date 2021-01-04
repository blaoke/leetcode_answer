#最长定差子序列
class Solution:
    def longestSubsequence(self, arr:[int], difference: int) -> int:
        difference=abs(difference)
        # arr=sorted(arr)
        arr=list(set(arr))
        arr.sort()
        print(list(arr),difference)
        b=[]
        for i in range(len(arr)-1):
            suum = 0
            target=arr[i]+difference
            for j in range(i+1,len(arr)):
                if arr[j]==target:
                    suum+=1
                    target+=difference
            b.append(suum)
        print(b)
        if max(b)==0 and difference==1:
            print(1)
        elif max(b)>0:
            print(max(b)+1)
        else:
            print(0)

a=Solution()
a.longestSubsequence(arr = [3,4,-3,-2,-4], difference = -5)
#有些问题