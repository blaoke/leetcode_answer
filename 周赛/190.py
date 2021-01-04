#5416
# class Solution:
#     def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
#         a=sentence.split(' ')
#         n=len(searchWord)
#         for i,item in enumerate(a):
#             if searchWord == item[:n]:
#                 return i+1
#         return -1
# a=Solution()
# print(a.isPrefixOfWord(sentence="i use triple pillow", searchWord ="pill"))

#5417
# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:
#         dic={'a','e','i','o','u'}
#         n=len(s)
#         l=0
#         res=0
#         tmp=len(list(filter(lambda x:x in dic,s[0:k])))
#         res=tmp
#         for r in range(k,n):
#             if s[l] in dic:
#                 tmp-=1
#             l+=1
#             if s[r] in dic:
#                 tmp+=1
#             res = max(res, tmp)
#         return res
# a=Solution()
# print(a.maxVowels(s="weallloveyou",k=7))

#5418

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# import collections
# class Solution:
#     def pseudoPalindromicPaths(self, root: TreeNode) -> int:
#         stack = []  # 存储单个满足条件的路径
#         res = []  # 存储所有路径
#         if not root:
#             return stack
#         def sums(root,stack):
#             stack.append(root.val)
#             if not root.left and not root.right: #访问到叶子节点
#                 res.append(stack[:])
#             if root.left:
#                 sums(root.left,stack)
#             if root.right:
#                 sums(root.right,stack)
#             stack.pop() #回溯法
#         sums(root,stack)
#         n=len(res)
#         ret=0 #返回的结果数
#         for i in range(n):
#             dic=collections.Counter(res[i])
#             even=filter(lambda x:x%2!=0,dic.values())
#             a=len(list(even))
#             if a==0 or a==1:
#                 ret+=1
#         return ret

#5419
#使用动态规划解决dp[i][j]为nums1前i个元素和nums2前j个元素点积能够形成的最大大和
class Solution:
    def maxDotProduct(self, nums1: [int], nums2: [int]) -> int:
        n1=len(nums1)
        n2=len(nums2)
        #一个全为正另一个全为负的情况
        if min(nums1)>0 and max(nums2)<0:
            return min(nums1)*max(nums2)
        if max(nums1)<0 and min(nums2)>0:
            return max(nums1)*min(nums2)
        dp=[[-10**5 for _ in range(n2+1)] for _ in range(n1+1)] #因为nums[i]范围为-1000到100,所以乘积最小值为-10**5
        for i in range(n1+1):
            dp[i][0]=0
        for j in range(n2+1):
            dp[0][j]=0
        for m in range(1,n1+1):
            for n in range(1,n2+1):
                #状态转移方程
                dp[m][n]=max(dp[m-1][n-1]+nums1[m-1]*nums2[n-1],dp[m-1][n],dp[m][n-1],nums1[m-1]*nums2[n-1])
        return dp[n1][n2]
a=Solution()
print(a.maxDotProduct(nums1 = [2,1,-2,5], nums2 = [3,0,-6]))


#
# class Solution:
#     def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
#         if min(nums1) > 0 and max(nums2) < 0:
#             return min(nums1) * max(nums2)
#         if min(nums2) > 0 and max(nums1) < 0:
#             return min(nums2) * max(nums1)
#         n, m = len(nums1), len(nums2)
#         f = [[-10 ** 9] * (m + 1) for _ in range(n + 1)]
#         for j in range(m):
#             f[0][j] = 0
#         for i in range(n):
#             f[i][0] = 0
#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 f[i][j] = max(nums1[i - 1] * nums2[j - 1] + f[i - 1][j - 1], f[i - 1][j], f[i][j - 1], f[i - 1][j - 1])
#         return f[n][m]


