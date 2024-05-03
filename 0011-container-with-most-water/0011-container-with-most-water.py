class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo =0
        hi = len(height)-1
        ma = 0
        wi = 0
        while lo<hi:
            wi = hi-lo
            if height[lo]<=height[hi]:
                ma = max(ma, wi*height[lo])
                lo+=1
            else:
                ma = max(ma, wi*height[hi])
                hi-=1
        return ma
            
        