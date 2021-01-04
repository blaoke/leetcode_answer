class Solution:
    def evalRPN(self, tokens: [str]) -> int:
        stack=[]
        a={'+','-','*','/'}
        for i in tokens:
            if i in a:
                right,left=int(stack.pop()),int(stack.pop())
                if i =='+':
                    stack.append(left+right)
                if i=='-':
                    stack.append(left-right)
                if i=='*':
                    stack.append(left*right)
                elif i=='/':
                    stack.append(int(left/right))
            else:
                stack.append(i)
        return int(stack[0])
a=Solution()
a.evalRPN(tokens= ["2", "1", "+", "3", "*"])
