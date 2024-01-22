class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = [0 for i in nums]
        res=[0,0]
        for i in nums:
            arr[i-1]+=1
        for i in range(len(arr)):
            if arr[i]>1:
                res[0] = i+1
            if arr[i]==0:
                res[1] = i+1
        return res
        