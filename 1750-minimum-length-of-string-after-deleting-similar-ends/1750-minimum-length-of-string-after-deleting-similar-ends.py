class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) -1
        while i < j:
            if s[i] != s[j]:
                break
            k = i
            while k < j-1:
                if s[k] == s[k+1]:
                    k += 1
                else:
                    break
            i = k
            k = j
            while k > i+1:
                if s[k] == s[k-1]:
                    k -= 1
                else:
                    break
            j = k
            i += 1
            j -= 1
        if i> j:
            return 0
        return j-i+1
        