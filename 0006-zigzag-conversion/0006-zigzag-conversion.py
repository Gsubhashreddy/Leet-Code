class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for i in range(numRows)]
        co = 0
        ind = 0
        add = True
        while ind < len(s):
            res[co].append(s[ind])
            if add:
                co+=1
            else:
                co-=1
            if co == numRows-1:
                add = False
            elif co == 0:
                add = True
            # print(res)
            ind+=1
            co %= numRows
        temp = ""
        for li in res:
            for ele in li:
                temp+=ele
        return temp
        