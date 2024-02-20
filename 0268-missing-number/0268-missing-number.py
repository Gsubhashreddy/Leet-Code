class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        le = len(nums)
        sum_n_numbers = (le* (le+1))//2
        curr_sum = 0
        for i in nums:
            curr_sum += i
        return sum_n_numbers - curr_sum
        