class Solution:
    def fourSumCount(self, A: [int], B: [int], C: [int], D: [int]) -> int:
        sums=[]
        sus={}
        a=0
        for i in range(len(A)):
            for j in range(len(B)):
                sums.append(A[i]+B[j])
        for i in range(len(C)):
            for j in range(len(D)):
                s=C[i]+D[j]
                if s not in sus:
                    sus[s]=1
                else:
                    sus[s]+=1
        for i in range(len(sums)):
                if -sums[i] in sus :
                    a+=sus[-sums[i]]

        print(sums)
        print(sus)
        print(a)


a=Solution()
# a.fourSumCount(A = [ -1,-1],B = [-1,1],C = [-1, 1],D = [ 1,-1])
a.fourSumCount(A = [ 1, 2],B = [-2,-1],C = [-1, 2],D = [ 0, 2])