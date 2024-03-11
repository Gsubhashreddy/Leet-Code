from io import StringIO
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # di = [-1 for i in range(26)]
        # for i in range(len(order)):
        #     di[ord(order[i])-ord('a')] = i
        # print(di)
        res = StringIO()
        di = {}
        for i in order:
            di[i] = True
        # res = ""
        di1 = {}
        for i in s:
            if i in di:
                di1[i] = di1.get(i,0) + 1
            else:
                res.write(i)
        for i in order:
            if i in s:
                tem = di1[i] * i
                res.write(tem)
                
        return res.getvalue()
        #     if 
        # return ""
        