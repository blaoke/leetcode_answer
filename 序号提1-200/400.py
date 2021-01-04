#本题与剑指offor44题相同,方法按照位数经行遍历,每遍历完一位,n减这一位的所有数字长度和,寻找到遍历的位数,
#找到在某一位的区间后,用剩余的n除以digit,求除数和余数,这一位的第一个元素+除数即为找到的这个数,这个数的第余数位就是结果
class Solution:
    def findNthDigit(self, n: int) -> int:
        def sums_numofdigit(digit):#当前位数所有的数字个数
            if digit==1:
                return 10
            else:
                return 9*(10**(digit-1))
        def start_num(digit): #这个位数开始的最小数字
            if digit==1:
                return 0
            else:
                return 10**(digit-1)
        def n_in_digit(n,digit):
            quotient,remainder=divmod(n,digit) #商和余数
            number=start_num(digit)+quotient
            return (number//(10**(digit-remainder-1)))%10 #求number从左向右的第remainder位(从0开始)

        digit=1
        while True:
            sums=sums_numofdigit(digit)#当前digit所有数字个数
            if n<sums*digit: #如果当前digit的所有数字长度大于n,说明结果在这个区间内
                return n_in_digit(n,digit)
            else:
                n -= sums * digit
                digit+=1

a=Solution()
print(a.findNthDigit(n=17))
