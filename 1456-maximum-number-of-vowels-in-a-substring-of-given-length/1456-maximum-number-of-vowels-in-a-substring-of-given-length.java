class Solution {
    public int maxVowels(String s, int k) {
        int co =0;
        int max = 0;
        for(int i=0;i<k;i++){
            char re = s.charAt(i);
            if (re == 'a' || re == 'e' || re == 'i' || re == 'o' || re == 'u') {
                co++;
            }
        }
        max = co;
        for(int i=k;i<s.length();i++){
            char re = s.charAt(i);
            if (re == 'a' || re == 'e' || re == 'i' || re == 'o' || re == 'u') {
                co++;
            }
            re = s.charAt(i-k);
            if (re == 'a' || re == 'e' || re == 'i' || re == 'o' || re == 'u') {
                co--;
            }
            max = Math.max(max,co);
        }
        return max;
        
        
    }
}