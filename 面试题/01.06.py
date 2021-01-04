class Solution:
    def compressString(self, S: str) -> str:
        n=len(S)
        if n==0:
            return ''
        ret=''
        i=0
        j=1
        while j < n:
            if S[i]==S[j]:
                j+=1
            else:
                ret=ret+S[i]+str(j-i)
                i=j
                j+=1
        ret+=S[i]+str(j-i)
        if len(ret)>=n:
            return S
        return ret