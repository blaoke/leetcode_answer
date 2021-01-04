#时间复杂度为O(1),如果n!=0,就将n与n-1做与运算,这样就会消掉左右边的1,而左边的1不变
class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res+=1
            n=n&n-1
        return res