#同剑指offor41题
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