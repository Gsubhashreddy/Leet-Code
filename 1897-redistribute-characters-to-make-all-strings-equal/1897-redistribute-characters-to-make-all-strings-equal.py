class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        di={}
        le=len(words)
        for word in words:
            for l in word:
                di[l]=di.get(l,0)+1
        for i in di:
            if di[i]%le!=0:
                return False
        return True
        