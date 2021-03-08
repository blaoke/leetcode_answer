#对撞指针法:i指针从0开始,j从n开始,两者不断向中间靠近

def twoSum( numbers: [int], target: int) -> [int]:
    i=0
    j=len(numbers)-1
    while i < len(numbers):
        if numbers[i]+numbers[j]<target:
            i+=1
        elif numbers[i]+numbers[j]>target:
            j-=1
        else:
            break
    return [i+1,j+1]

print(twoSum(numbers = [2, 7, 11, 15], target = 18))