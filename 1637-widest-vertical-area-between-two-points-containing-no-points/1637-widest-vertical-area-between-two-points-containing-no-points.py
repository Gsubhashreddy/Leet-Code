class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        ma=-1
        for i in range(len(points)-1):
            ma=max(ma,(points[i+1][0]-points[i][0]))
        return ma
            
        