class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return int(x)
        else:
            l=1
            r=x/2
            while l<=r:
                mid=int(l+(r-l)/2)
                if x==mid*mid:
                    return mid
                elif x>mid*mid:
                    l=mid+1
                else:
                    r=mid-1
            return int(r)
                

        