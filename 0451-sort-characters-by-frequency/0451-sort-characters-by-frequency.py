class Solution:
    def frequencySort(self, s: str) -> str:
        di ={}
        for i in s:
            di[i] = di.get(i,0)+1
        # print(di)
        di1={}
        for i in di:
            val = di[i]
            if val not in di1:
                di1[val] = [i]
            else:
                temp = di1[val]
                temp.append(i)
                di1[val] = temp
        li = []
        for k,v in di1.items():
            li.append([k,v])
        res = sorted(li, key= lambda x : x[0], reverse = True)
        re = ""
        for i in res:
            for j in i[1]:
                temp = j * i[0]
                re +=temp
        # print(re)
        return re