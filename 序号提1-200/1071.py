class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
            return ''
        a=len(str1)
        b=len(str2)
        #在a,b有最大公因子的情况下,求最大公因子
        if a<b:
            a,b=b,a
        while a%b:
            a,b=b,a%b
        return str1[:b]