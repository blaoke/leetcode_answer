#定义两个指针i,j一个在开头,一个在结尾,如果i!=j就向后遍历,知道[0:i]的值等于[]j:,则遍历结束
class Solution:
    def canThreePartsEqualSum(self, A: [int]) -> bool:
        n=len(A)
        sums=sum(A)
        if sums%3!=0:
            return False
        sum1=A[0]
        sum2=A[n-1]
        i=0
        j=n-1
        while j-i>1:
            if sum1==sum2==sums/3:
                return True
            if sum1!=sums/3:
                i+=1
                sum1+=A[i]
            if sum2!=sums/3:
                j-=1
                sum2+=A[j]
        return False

a=Solution()
print(a.canThreePartsEqualSum(A=[3,3,6,5,-2,2,5,1,-9,4]))

