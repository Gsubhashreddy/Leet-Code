class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = ""
        flag = False
        for i in range(len(word)):
            if word[i] == ch:
                res = word[i] + res
                res+=word[i+1:]
                flag = True
                break
            else:
                res = word[i] + res
                # print(res)
        if flag:
            return res
        return word
        