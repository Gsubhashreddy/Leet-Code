class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # we need 2 hashmaps
        # First we check if element is there in it.
        #If present, get index increment by 1 and use this index to insert element into new hasMap
        di={}
        re={}
        res=[]
        for i in nums:
            if i in di:
                #Pass
                di[i]+=1
            else:
                di[i]=1
            temp=re.get(di[i],[])
            temp.append(i)
            re[di[i]] = temp
        for j in re:
            res.append(re[j])
        return res
        