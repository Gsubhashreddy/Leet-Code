class Solution:
    def minOperations(self, s: str) -> int:
        s0=0
        for i in range(len(s)):
            if i%2==0:
                if s[i]=="1":
                    s0+=1
            else:
                if s[i]=="0":
                    s0+=1
        return min(s0, len(s)-s0)