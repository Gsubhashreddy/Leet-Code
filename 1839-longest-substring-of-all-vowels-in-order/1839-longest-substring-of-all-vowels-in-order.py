class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vow = "aeiou"
        po = -1
        st = 0
        ma = 0
        
        for i in range(len(word)):
            if po == -1 and word[i] == 'a':
                po = 0
                st = i
            elif po >= 0 and word[i] == vow[po]:
                if po == 4:
                    ma = max(ma, i - st + 1)
            elif po < 4 and word[i] == vow[po + 1]:
                po += 1
                if po == 4:
                    ma = max(ma, i - st + 1)
            else:
                if word[i] == 'a':
                    po = 0
                    st = i
                else:
                    po = -1
            
            # Debugging logs
            # print(f"i: {i}, word[i]: {word[i]}, po: {po}, st: {st}, ma: {ma}")

        return ma

# # Test the solution
# solution = Solution()
# print(solution.longestBeautifulSubstring("aeeeiiiioooauuuaeiou"))
