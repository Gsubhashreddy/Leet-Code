class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        fma,sma=0,0
        fmi,smi=10000000,1000000
        for i in nums:
            if i>fma:
                sma=fma
                fma=i
            elif i>sma:
                sma=i
            if i<fmi:
                smi=fmi
                fmi=i
            elif i< smi:
                smi=i

        return (fma*sma) - (fmi*smi)