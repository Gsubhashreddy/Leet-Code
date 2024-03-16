class Solution {
    public int longestOnes(int[] nums, int k) {
        int st =0;
        int end = 0;
        int co = 0;
        int ma = 0;
        while(end < nums.length){
            int num = nums[end];
            if(num == 0){
                if(k>0){
                    k--;
                    end++;
                    co++;
                }
                else{
                    if(nums[st]==0){
                        k++;
                        
                    }
                    co--;
                    st++;
                }
            }
            else{
                end++;
                co++;
            }
            ma = Math.max(ma,co);
        }
        return ma;
        
    }
}