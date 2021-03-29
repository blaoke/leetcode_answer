#巧妙方法
class Solution:
    def replaceSpace(self, s: str) -> str:
        s.split(' ')
        res = ''
        for i in s.split(' '):
            res += i + '%20'
        return res[:-3]
#一般方法
class Solution:
    def replaceSpace(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)) :
            if s[i] == ' ':
                s[i] = '%20'
        return ''.join(s)

#除了应用上面python自带的巧妙方法外，常规方法如下
#首先遍历一遍字符串，统计空格数目，然后将字符串长度拉长到可以放%20的长度，然后定义两个指针，分别从前向后移动，如果遇到空格就添加上%20
class Solution:
    def replaceSpace(self, s: str) -> str:
        space_num=0
        n=len(s)
        for i in s:
            if i==' ':
                space_num+=1
        p1=n-1 #p1指向原来字符串末尾
        s=s+' '*space_num*2
        p2=len(s)-1 #p2指向增加长度后的字符串长度末尾
        s=list(s)
        while p1!=p2:
            if s[p1]!=' ':
                s[p2]=s[p1]
                p1-=1
                p2-=1
            else:
                s[p2]='0'
                p2-=1
                s[p2]='2'
                p2 -= 1
                s[p2] = '%'
                p2-=1
                p1-=1
        return ''.join(s)
a=Solution()
b=a.replaceSpace(s="We are happy.")
print(b)


