#双指针撞击法,小的边不断向大的边靠近
def maxArea( height: [int]) -> int:
    smax=0
    l=0
    r=len(height)-1
    while l<r:
        smax=max(smax,(r - l) * min(height[r], height[l]))
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    print(smax)

maxArea(height=[1,8,6,2,5,4,8,3,7])


