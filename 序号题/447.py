class Solution:
    def lens(self, a: [int], b: [int]):
        return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
    def numberOfBoomerangs(self, points: [[int]]) -> int:
        sums=0
        for i in range(len(points)):
            a={}
            for j in range(len(points)):
                if j!=i:
                    d=self.lens(points[i],points[j])
                    a[d]=a.get(d,0)+1
            for k in a.values():
                # if a[k]>1:
                sums+=k*(k-1)
        print(sums)

a=Solution()
a.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]])
#  a.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]])

