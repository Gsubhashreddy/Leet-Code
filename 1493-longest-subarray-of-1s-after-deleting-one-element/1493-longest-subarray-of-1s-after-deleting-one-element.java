class Solution {
    public int longestSubarray(int[] nums) {
        int st =0;
        int end = 0;
        int co =0;
        int max = 0;
        int ze = 1;
        boolean del = false;
        while(end<nums.length){
            if(nums[end]==0){
                del = true;
                if(ze==1){
                    ze=0;
                    end++;
                }
                else{
                    if(nums[st]==0) ze=1;
                    else co--;
                    st+=1;
                }
            }
            else{
                co++;
                end++;
                
            }
            max = Math.max(max,co);
            
        }
        if(del==false)return max-1>0 ? max-1 : 0;
        return max;
        
    }
}