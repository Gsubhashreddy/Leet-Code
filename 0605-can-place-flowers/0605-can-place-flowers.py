class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ne = len(flowerbed)
        if n== 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                if i-1>=0:
                    flowerbed[i-1] = -1
                if i+1 < ne:
                    flowerbed[i+1] = -1
        i = 0
        while n > 0 and i < ne:
            if flowerbed[i] == 0:
                if i-1>=0:
                    flowerbed[i-1] = -1
                if i+1 < ne:
                    flowerbed[i+1] = -1
                n -= 1
            i+=1
        if n>0:
            return False
        return True
        