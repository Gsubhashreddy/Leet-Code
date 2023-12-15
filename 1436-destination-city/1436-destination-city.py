class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        di={}
        res=""
        for path in paths:
            di[path[0]]= True
        for path in paths:    
            if path[1] not in di:
                return path[1]
        return res
        