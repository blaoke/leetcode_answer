#方法一:自己方法
class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(n):
            strs=str(n)
            res=0
            for i in strs:
                res+=int(i)**2
            return res



        for j in range(100):
            if happy(n)==1:
                return True
            else:
                n=happy(n)
                happy(n)
        return False
a=Solution()
print(a.isHappy(n=19))


#方法二:官方方法,使用哈希表存储没有访问到的数字,如果有访问到说明存在环,退出
class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(n): #使用divmod()方法求数的每一位值的方法值得学习
            total=0
            while n>0:
                n,digit=divmod(n,10)
                total+=digit**2
            return total
        stack=set()
        while n!=1 and  n not in stack:
            stack.add(n)
            n=happy(n)
        return n==1

#方法三:使用快慢指针,slow每次前进一步,fast每次前进两步,最终如果fast追上slow说明有环,如果fast==1,说明是快乐数
class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(n): #使用divmod()方法求数的每一位值的方法值得学习
            total=0
            while n>0:
                n,digit=divmod(n,10)
                total+=digit**2
            return total
        slow=n
        fast=happy(n)
        while fast!=1 and fast!=slow:
            slow=happy(slow)
            fast=happy(happy(fast))
        return fast==1

