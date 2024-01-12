class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        res=0
        le=len(s)//2
        for i in range(le):
            if s[i]=='a' or s[i]=='e' or s[i]=='o' or s[i]=='i' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='O' or s[i]=='I' or s[i]=='U':
                res+=1
        for i in range(le,len(s)):
            if s[i]=='a' or s[i]=='e' or s[i]=='o' or s[i]=='i' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='O' or s[i]=='I' or s[i]=='U':
                res-=1
        if res==0:
            return True
        return False