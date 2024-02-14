class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(i)
            else:
                neg.append(i)
        print(pos,neg)
        p, n = 0,0
        res = []
        curr = "pos"
        while p< len(pos) and n < len(neg):
            if curr == "pos":
                res.append(nums[pos[p]])
                p+=1
                curr = "neg"
            else:
                res.append(nums[neg[n]])
                n+=1
                curr = "pos"
        if p< len(pos):
            res.append(nums[pos[p]])
        else:
            res.append(nums[neg[n]])
        return res
            
        