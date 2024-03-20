class Solution {
    public int pivotIndex(int[] nums) {
        int[] res = new int[nums.length];
        int su = 0;
        
        for(int i=1; i<nums.length;i++){
            su+= nums[i-1];
            res[i] = su;
        }
        // System.out.println(Arrays.toString(res));
        su+= nums[nums.length-1];
        for(int i=0; i<nums.length;i++){
            su -= nums[i];
            if(su == res[i]) return i;
        }
        return -1;
    }
}