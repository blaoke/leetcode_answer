#与主站264题目相同
# 用空间换时间,初始化一个长度为n的数组,第一个丑数为1,p2,p3,p5分别指向2,3,5的倍数,下一个丑数为p2,p3,p5对应元素分别与2,3,5相乘的最小值,如果分别乘积小于当前丑数,p(2,3,5)就+1
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly=[1 for _ in range(n)]
        p2,p3,p5=0,0,0
        next_ugly_index=1 #下一个丑数下标索引
        while next_ugly_index<n:
            next_ugly=min(ugly[p2]*2,ugly[p3]*3,ugly[p5]*5)
            ugly[next_ugly_index]=next_ugly
            while ugly[p2]*2<=next_ugly:
                p2+=1
            while ugly[p3]*3<=next_ugly:
                p3+=1
            while ugly[p5]*5<=next_ugly:
                p5+=1

            next_ugly_index+=1
        return ugly[-1]

