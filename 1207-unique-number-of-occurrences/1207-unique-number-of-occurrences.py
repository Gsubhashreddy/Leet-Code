class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        di={}
        co={}
        for i in arr:
            di[i]=di.get(i,0)+1
            
        for key,value in di.items():
            co[value]=co.get(value,0)+1
            if co[value]>1:
                return False
        return True
            
        