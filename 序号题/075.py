#方法一，利用计数器,统计0，1，2的个数，然后分别进行赋值
def sortColors(nums:[int]):
    n=len(nums)
    a=b=c=0
    for i in range(n):
        if nums[i] == 0:
            a+=1
        elif nums[i]==1:
            b+=1
        else:
            c+=1
    index=0
    for i in range(a):
        nums[index]=0
        index+=1
    for j in range(b):
        nums[index]=1
        index+=1
    for k in range(c):
        nums[index]=2
        index+=1
    # for i in range(a):
    #     nums[i]=0
    # for j in range(a,a+b):
    #     nums[j]=1
    # for k in range(a+b,n):
    #     nums[k]=2
    print(nums)
sortColors(nums=[2,2,1,0,1,0])

#方法二：利用三路快排，设置索引点，zero,i,two,nums[i]=1时不变，
# nums[i]<1时与nums[zero]交换位置，nums[i]>1时与nums[two]交换位置
def sortColors(nums:[int]):
    zero=-1
    two=len(nums)
    i=0
    while i <two:
        if nums[i]<1:
            zero+=1
            nums[zero],nums[i]=nums[i],nums[zero]
            i+=1
        elif nums[i]>1:
            two-=1
            nums[i],nums[two]=nums[two],nums[i]
        else :
            i+=1
    print(nums)
sortColors(nums=[2,2,1,0,1,0])


