class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double max = 0;
        double curr = 0.0;
        for(int i =0; i< k;i++){
            curr+=nums[i];
        }
        max = curr/k;
        for(int i =k;i<nums.length;i++){
            curr += nums[i];
            curr -= nums[i-k];
            max = Math.max(curr/k, max);
        }
        return max;
        
    }
}