from io import StringIO
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        words = StringIO()
        l1 = len(word1)
        l2 = len(word2)
        p1 = 0
        p2 = 0
        while p1 < l1 and p2 < l2:
            # if word1[p1] < word2[p2]:
            words.write(word1[p1])
            p1 += 1
            # else:
            words.write(word2[p2])
            p2 += 1
        if p2 < l2:
            for i in range(p2,l2):
                words.write(word2[i])
        else:
            for i in range(p1,l1):
                words.write(word1[i])
        return words.getvalue()