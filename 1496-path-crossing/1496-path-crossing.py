class Solution:
    def isPathCrossing(self, path: str) -> bool:
        di={(0,0):True}
        cur=[0,0]
        for i in path:
            if i=="N":
                temp=(cur[0],cur[1]+1)
            elif i=="S":
                temp=(cur[0],cur[1]-1)
            elif i=="E":
                temp=(cur[0]+1,cur[1])
            else:
                temp=(cur[0]-1,cur[1])
            if temp in di:
                return True
            di[temp]=True
            cur=temp
        return False
                
                
        