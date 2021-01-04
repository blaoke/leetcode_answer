class Solution:
    def merge(self, A:list, m: int, B:list, n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        a=0#指向A的指针,
        b=0#指向B的指针
        res=[]
        while a<m and b<n:
           if A[a]<=B[b]:
               res.append(A[a])
               a+=1
           else:
               res.append(B[b])
               b+=1
        while a<m:
            res.append(A[a])
            a+=1
        while b<n:
            res.append(B[b])
            b+=1
        A[:] = res
        print(A)

s=Solution()
s.merge(A = [1,2,3,0,0,0,0,0,0,0], m = 3,B = [2,5,6], n = 3)


