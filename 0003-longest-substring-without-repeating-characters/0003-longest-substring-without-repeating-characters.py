class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        st, end = 0, 0
        di = {}
        co = 0
        while end < len(s):
            if s[end] not in di:
                co += 1
                di[s[end]] = True
                res = max(co, res)
            else:
                # print(di)
                while s[st] != s[end]:
                    del di[s[st]]
                    co -= 1
                    st += 1
                # del di[s[st]]
                # co -= 1
                st += 1
            end += 1
        return res
                
            
        