class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
         # Dictionary to track the frequencies of elements
        freq_map = Counter(arr)

        # List to track all the frequencies
        frequencies = list(freq_map.values())
        
        frequencies.sort()
        
        co = 0
        for i in range(len(frequencies)):
            co += frequencies[i]
            
            if co > k:
                return len(frequencies)- i
        return 0
        # Sorting the frequenc