class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        res = 0
        i = 0
        tlen = len(t)
        slen = len(s)
        j = 0
        while i <tlen and j< slen:
            if s[j] == t[i]:
                i+=1
            j+=1
        return tlen - i
        