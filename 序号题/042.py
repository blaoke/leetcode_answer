#方法一:利用栈解决
class Solution:
    def trap(self, height: [int]) -> int:
        n=len(height)
        res=0
        stack=[]
        for i in range(n):
            while stack and height[stack[-1]]<height[i]:
                floor=stack.pop() #这个是装雨水的底
                while stack and height[floor]==height[stack[-1]]: #如果栈顶的元素和底元素相同,就一起去除
                    stack.pop()
                if not stack:
                    break
                high=min(height[stack[-1]],height[i])-height[floor] #高度为两边的最小值减去底
                wide=i-stack[-1]-1  #宽度为两个高之间的距离-1
                res+=high*wide

            stack.append(i)
        return res
a=Solution()
print(a.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]))

#方法二:分别从左向右和从右向左,后面的面积都等于前面柱子的最大值,分别将2者加起来,可以发现柱子和积水加了两遍,减去柱子面积就是积水面积
# https://leetcode-cn.com/problems/trapping-rain-water/solution/wei-en-tu-jie-fa-zui-jian-dan-yi-dong-10xing-jie-j/
class Solution:
    def trap(self, height: [int]) -> int:
        maxleft=0
        maxright=0
        area_millow=0 #表示柱子面积
        res=0 #从左向右和从右向左的面积和
        n=len(height)
        for i in range(n):
            maxleft=max(maxleft,height[i])
            maxright=max(maxright,height[-(i+1)])
            res+=maxright+maxleft
            area_millow+=height[i]
        res-=area_millow+n*maxleft #遍历完之后maxleft/maxright都表示最长的柱子
        return  res
a=Solution()
print(a.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]))

#方法三:利用双指针解决,left 和right 表示从左向右 和 从右向左移动的指针
#定义 left_max 和 right_max 分别表示 从左向右的最大值 和 从右向左的最大值,
#如果left_max<right_max 并且left的值小于left_max,不管left右边的值如何,left这个位置一定可以装雨水,
#同理如果left_max>right_max并且 right 值小于 right_max 表示right这个位置可以装雨水
class Solution:
    def trap(self, height: [int]) -> int:
        n=len(height)
        left=0
        right=n-1
        left_max=right_max=0
        res=0 #用于存储结果
        while left<=right:
            if left_max<right_max:
                if height[left]<left_max:
                    res+=left_max-height[left]
                left_max=max(height[left],left_max)
                left+=1
            else:
                if right_max>height[right]:
                    res+=right_max-height[right]
                right_max=max(height[right],right_max)
                right-=1
        return res

a=Solution()
print(a.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]))