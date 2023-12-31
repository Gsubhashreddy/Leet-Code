class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        di={}
        ma=-1
        for i in range(len(s)):
            if di.get(s[i],-1)!=-1:
                te=i-di[s[i]]-1
                ma=max(ma,te)
            else:
                di[s[i]]=i
        return ma
                
        