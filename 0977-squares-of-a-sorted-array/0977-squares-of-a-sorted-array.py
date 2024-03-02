class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        res = [0 for i in nums]
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                squ = nums[right]
                right  -= 1
            else:
                squ = nums[left]
                left +=1
            res[i] = squ ** 2
        return res
        