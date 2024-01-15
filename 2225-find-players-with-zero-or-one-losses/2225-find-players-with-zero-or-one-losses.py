class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win={}
        los={}
        
        for i in matches:
            wi=i[0]
            lo=i[1]
            los[lo]=los.get(lo,0)+1
            if lo in win:
                win.pop(lo)
            if wi not in los:
                win[wi]=win.get(wi,0)+1
            else:
                if wi in win:
                    win.pop(wi)
        winArr=[]
        losArr=[]
        for i in win:
            winArr.append(i)
        for i in los:
            if los[i]==1:
                losArr.append(i)
        winArr.sort()
        losArr.sort()
        return [winArr,losArr]
                
        