class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        maximumToken = 0
        tokens.sort()
        le = len(tokens)
        lo = 0
        hi = le -1
        currToken = 0
        for i in range(le):
            if power >= tokens[lo]:
                power -= tokens[lo]
                lo += 1
                currToken += 1
                maximumToken = max(maximumToken, currToken)
            elif currToken >= 1:
                currToken -= 1
                power += tokens[hi]
                hi -= 1
            else:
                break
        return maximumToken
        