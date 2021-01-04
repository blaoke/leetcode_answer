#方法一:分治算法,找到数组中最小值,最小值*长度=res,之后从最小值两边出发,分别寻找各自的最小值*长度=res,求max(res)
#结果最后2个测试用例通过不了
class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        n=len(heights)
        def fenzhi(left,right,heights):
            if left>=right:
                return 0
            else:
                mins=min(heights[left:right])
                locate=left+heights[left:right].index(mins) #最小值在数组中的索引
                return max(mins*(right-left),fenzhi(left,locate,heights),fenzhi(locate+1,right,heights))
        return fenzhi(0,n,heights)
a=Solution()
print(a.largestRectangleArea(heights=[2,1,5,6,2,3]))

#方法二:单调栈,类似042题目,存储一个递增单调栈,如果当前元素小于栈顶元素,就将栈顶元素弹出,继续比较当前元素与栈顶元素,直到当前元素大于栈顶元素为止,
#求栈顶元素到当前元素的最小高度*距离,与存储的res比较更新res
class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        stack=[]
        heights=[0]+heights+[0]
        n = len(heights)
        res=0
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                top=stack.pop()
                res=max(res,(i-stack[-1]-1)*heights[top])
            stack.append(i)
        return res


