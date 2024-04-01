class Solution {
    public int lengthOfLastWord(String s) {
        int flag = 0;
        int res = 0;
        for(int i = s.length()-1; i>=0; i--){
             if(s.charAt(i) == ' ' && flag!=0) {
                break;
            }
            if(s.charAt(i) != ' ') {
                flag = 1;
                res++;
            }
            
        }
        return res;
        
    }
}