class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        res = []
        i=0
        curr = intervals[0]
        flag = False
        while i < len(intervals)-1:
            # Case 1 second interval is inside first
            # i.e if i[1] >= i+1 [1]
            if curr[1] >= intervals[i+1][1]:
                i+=1    #Curr remains same and skip next element
                
            elif curr[1] >= intervals[i+1][0]:
                curr[1] = intervals[i+1][1]
                i+=1
            
            else:
                res.append(curr)
                flag = True
                i+=1
                if i < len(intervals)-1:
                    curr = intervals[i]
                    flag =False
                elif i == len(intervals)-1:
                    res.append(intervals[i])
        if not flag:
            res.append(curr)
        return res
        