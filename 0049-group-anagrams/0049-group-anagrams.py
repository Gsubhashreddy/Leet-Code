class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di ={}
        for i in strs:
            res = ''.join(sorted(i))
            # print(res)
            if res in di:
                temp = di[res]
                temp.append(i)
                di[res] = temp
            else:
                di[res] = [i]
        re=[]
        for i in di:
            re.append(di[i])
        return re
        