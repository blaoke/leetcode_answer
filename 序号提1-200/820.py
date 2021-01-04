#自己方法:从前到后,将每一个单词入栈,res加上这个入栈的长度,然后后一个单词从后向前与栈顶元素比对,如果这个单词全部比对正确,就将res减去比对的长度
#如果比对错误,res+1表示#,将栈清空,下一个入栈(最后几个测试用例通过不了,因为每个单词的顺序不固定,而一味地排序不能解决所有情况)
class Solution:
    def minimumLengthEncoding(self, words: [str]) -> int:
        words.sort(key=len,reverse=-1)
        n=len(words)
        if n==0:return 0
        if n==1:return len(words[0])+1
        res=0
        for i in range(n-1):
            words[i].split(',')
            words[i+1].split(',')
            a=list(words[i]) #['t', 'i', 'm','e']
            b=list(words[i+1]) #['i','m','e']
            lena=len(a)
            lenb=len(b)
            last=False
            res+=lena
            while len(b)>0 and len(a)>0:
                topb=b.pop()
                topa=a.pop()
                if topa==topb:
                    continue
                else:
                    res+=1 #如果不能全部匹配,就退出,并res+1(#)
                    last=True
                    break
            if len(b)==0 and last==False:
                res-=lenb-len(b) #res将去匹配的长度
        return res+1+len(words[n-1])
a=Solution()
print(a.minimumLengthEncoding(words=["time", "me", "bell"]))

#方法二(官方暴力解法):将所有单词存入集合,然后对每一个单词从前往后遍历,如果单词的后缀在集合中,就将这个单词从集合中删除
class Solution:
    def minimumLengthEncoding(self, words: [str]) -> int:
        ret=set(words)
        for word in words:
            for i in range(1,len(word)):
                ret.discard( word[i:])
        return sum(len(word)+1 for word in ret)

#方法三:构建 字典树,单词从后往前面入树

