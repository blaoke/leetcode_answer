#同主站233题
#n = xyzdabc，此时我们求千位是 1 的个数，也就是 d 所在的位置。那么此时有三种情况，
# d == 0，那么千位上 1 的个数就是 xyz * 1000
# d == 1，那么千位上 1 的个数就是 xyz * 1000 + abc + 1
# d > 1，那么千位上 1 的个数就是 xyz * 1000 + 1000
# 定义
# 1.表示当前位置分位的digit
# 2.表示高于当前位数的数字high
# 3.表示低于当前位数的数字low
# 4.表示当前位置数的cur
# 遍历数字每个位置,累加每个位置为1的情况
# 每个位置的为一的情况又分3中情况
# 1. 如果为0,则count=high*digit
# 2. 为1,则count=high*digit+low+1
# 3. 大于1,count=(high+1)*digit
class Solution:
    def countDigitOne(self, n: int) -> int:
        lens=len(str(n))
        count=0
        for i in range(lens):
            digit=10**i #当前位置所在的位(是十分位,百分位,还是千分位等)
            high=n//(digit*10) #高于当前位的数字
            low=n%digit #低于当前位的数字
            cur=(n//digit)%10 #当前位置的数字
            if cur==0: #当前位为0
                count+=high*digit
            elif cur==1: #当前为为1
                count+=high*digit+low+1
            else: #当前位大于1
                count+=(high+1)*digit
        return count
a=Solution()
print(a.countDigitOne(n=93))

