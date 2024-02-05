class Solution:
    def firstUniqChar(self, s: str) -> int:
       
        di={}
        for i in s:
            di[i]= di.get(i,0)+1
        
        for i in range(len(s)):
            if di[s[i]]==1:
                return i
        return -1
        