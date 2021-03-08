#方法一:用二分法不断逼近,直到猜出那个值
class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        res=0
        while l<=r:
            mid=(l+r)//2
            if mid*mid>x:
                r=mid-1
            else:
                l=mid+1
                res=mid #这个地方有个陷阱,res应该永远存储的是左边的值,因为是向下取整
        return res

a=Solution()
print(a.mySqrt(x=9))   

#方法二:牛顿法,每次用过这个点的斜率直线逼近,x1=0.5*(x0+c/x0)
class Solution:
    def mySqrt(self, x: int) -> int:
        x0=x
        while x0*x0>x:
            x1=0.5*(x0+x/x0)
            x0=x1
        return x0