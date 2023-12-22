class Solution:
    def maxScore(self, s: str) -> int:
        l=0
        r=0
        ma=-1
        if s[0]=="0":
            l+=1
        if s[-1]=="1":
            r+=1
        for i in range(1, len(s)-1):
            if s[i]=="1":
                r+=1
        ma=max(ma,(l+r))
        for i in range(1,len(s)-1):
            if s[i]=='0':
                l+=1
            elif s[i]=='1':
                r-=1
            ma=max(ma,(l+r))
        return ma    
        
        