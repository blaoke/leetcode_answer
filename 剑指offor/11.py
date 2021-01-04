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



        # [2, 2, 2, 0, 1]