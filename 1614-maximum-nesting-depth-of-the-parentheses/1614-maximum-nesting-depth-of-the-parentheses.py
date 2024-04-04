class Solution:
    def maxDepth(self, s: str) -> int:
        ma = 0
        cu = 0
        for i in s:
            if i == "(":
                cu += 1
                ma = max(ma, cu)
            elif i == ")":
                cu -= 1
        return ma
                
        