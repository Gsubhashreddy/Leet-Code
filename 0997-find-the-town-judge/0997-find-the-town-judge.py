class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # res = [0 for i in range(n+1)]
        # le = len(trust)
        if n == 1:
            return 1
        res = {}
        res1 = {}
        for rel in trust:
            res1[rel[0]] = True
            if rel[1] in res:
                temp = res[rel[1]]
                temp.append(rel[0])
                res[rel[1]] = temp
            else:
                res[rel[1]] = [rel[0]]
        print(res)
        for i in res:
            if len(res[i]) == n -1 and i not in res1:
                return i
        
        
        return -1
        