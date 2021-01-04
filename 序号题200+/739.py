#方法:利用栈解决,小于栈顶就入栈,大于栈顶就出栈
class Solution:
    def dailyTemperatures(self, T: [int]) -> [int]:
        n = len(T)
        res=[0 for _ in range(n)]
        stack=[]

        stack.append([0, T[0]])
        for i in range(1,n):
            while stack and stack[-1][1] < T[i]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append([i, T[i]])
        return res

a=Solution()
print(a.dailyTemperatures(T= [73, 74, 75, 71, 69, 72, 76, 73]))
