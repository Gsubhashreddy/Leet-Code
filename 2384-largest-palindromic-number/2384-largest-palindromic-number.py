class Solution:
    def largestPalindromic(self, num: str) -> str:
        di = {}
        for i in num:
            di[i] = di.get(i,0)+1
        front = ""
        back = ""
        mid = ""
        for i in range(9,-1,-1):
            a = str(i)
            if a in di:
                res = di[a] // 2
                rem = di[a] %2
                front += res*a
                back = (res*a) + back
                
                if rem == 1 and len(mid)==0:
                    mid = a
        if len(front)>=1 and front[0] == '0':
            if mid == "":
                return '0'
            return mid
        return front+mid+back
                    
                
        
            
        