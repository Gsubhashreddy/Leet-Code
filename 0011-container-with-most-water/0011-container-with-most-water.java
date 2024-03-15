class Solution {
    public int maxArea(int[] height) {
        
        // Max of min of pairs
        // difference of pairs * width should be maximum
        // 2 For loops - O(n**2)
        // Which Pointer to move
        int lo= 0;
        int hi = height.length -1;
        int maxi = 0;
        while(lo<hi){
            int width = hi-lo;
            int hei = Math.min(height[lo], height[hi]);
            maxi = Math.max(maxi, hei*width);
            if(height[lo]<= height[hi]){
                lo++;
            }
            else hi--;
        }
        return maxi;
        
    }
}