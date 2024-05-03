class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        co = 0
        end = 0
        st = 0
        le = len(s)
        di = {}
        while end < le:
            di[s[end]] = di.get(s[end],0)+1
            while di[s[end]] > 1:
                di[s[st]] -= 1
                # if di[st] == 0:
                st+=1
            co = max(co,(end-st+1))
            end+=1
        return co
                    
            
        