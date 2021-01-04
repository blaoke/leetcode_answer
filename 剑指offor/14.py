#n大于5时,将n分成3的倍数越多,乘积越大,如果最后剩余1,表示前一个分割为4,需要将4分为2个2,而不是1和3
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        num3 = n // 3
        res = n - num3 * 3
        if res == 1:
            num3 -= 1
        num2 = (n - num3 * 3) //2
        return int(3 ** num3 * 2 ** num2)%1000000007


