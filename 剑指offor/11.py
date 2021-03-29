#同154题
class Solution:
    def minArray(self, numbers: [int]) -> int:
        n=len(numbers)
        left=0
        right=n-1
        if numbers[left]<numbers[right]:
            return numbers[0]
        mid=(left+right)//2
        while right-left>1:
            if numbers[mid]==numbers[left]==numbers[right]: #在遇到[10,1,10,10,10] 这种情况时,只能从前往后遍历
                mins=numbers[left]
                for i in range(left+1,right):
                    if numbers[i]<mins:
                        mins=numbers[i]
                return mins

            if numbers[mid]>=numbers[left]:
                left=mid
            else:
                right=mid
            mid = (left + right) // 2
        return numbers[right]

a=Solution()
print(a.minArray(numbers=[1,1,1,0,1,1,1,1,1]))

#二分法思想：
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        size = len(numbers)
        if size == 0:
            return 0

        left = 0
        right = size - 1

        while left < right:
            mid = (left + right) // 2

            if numbers[mid] > numbers[right]:
                # [3, 4, 5, 1, 2]，mid 以及 mid 的左边一定不是最小数字
                # 下一轮搜索区间是[mid + 1, right]
                left = mid + 1
            elif numbers[mid] == numbers[right]:
                # 只能把 right 排除掉，下一轮搜索区间是[left, right - 1]
                right = right - 1
            else:
                # 此时 numbers[mid] < numbers[right]
                # mid 的右边一定不是最小数字，mid 有可能是，下一轮搜索区间是[left, mid]
                right = mid
        return numbers[left]


#投巧方法
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        number=list(set(numbers))
        number.sort(key=numbers.index)
        n=len(number)
        pre=number[0]
        mins=number[0]
        for i in range(1,n):
            if number[i]<pre:
                return number[i]
            else:
                mins=min(mins,number[i])
            pre=number[i]
        return mins