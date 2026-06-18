class Solution:
    def mySqrt(self, x: int) -> int:

        l,r = 0,x

        while l <= r:

            mid = (l+r)//2

            temp = mid*mid

            if temp == x:
                return mid
            
            elif temp < x:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return r
        