class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z

        def gcd(x,y):
            small=min(x,y)
            while small:
                if x%small==0 and y%small ==0:
                    return small
                else:
                    small-=1
        return z % gcd(x, y) == 0



