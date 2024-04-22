from collections import defaultdict 
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        di = defaultdict(int)
        for i in candyType:
            di[i]+=1
        n = len(candyType)//2
        if len(di) > n:
            return n
        return len(di)
        