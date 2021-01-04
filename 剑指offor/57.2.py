class Solution:
    def findContinuousSequence(self, target: int) -> [[int]]:
        small=1#指向底的指针
        big=2#指向头的指针
        if target<3:
            return []
        mid=target//2
        res=[]
        sums=small+big
        while (small<=mid):
            if sums==target:
                res.append([i for i in range(small,big+1)])
            while sums>target:
                sums-=small
                small+=1
                if sums==target and small<=mid:
                    res.append([i for i in range(small,big+1)])
            big+=1
            sums+=big
        return res