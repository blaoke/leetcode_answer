#方法一:可以通过90%的测试,后面的测试超时
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        res=0
        B=set()
        for i in A:
            if i not in B:
                B.add(i)
            else:
                while i in B:
                    i+=1
                    res+=1
                B.add(i)
        return res
#方法二: 先将数组排序,然后从前往后遍历,如果当前元素小于等于前一个元素,就将当前元素变成前一个元素加1
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        res=0
        A.sort()
        for i in range(1,len(A)):
            if A[i]<=A[i-1]:
                pre=A[i]
                A[i]=A[i-1]+1
                res+=A[i]-pre
        return res


