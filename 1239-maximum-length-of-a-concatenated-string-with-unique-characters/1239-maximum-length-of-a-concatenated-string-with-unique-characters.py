class Solution:
    def maxLength(self, arr: List[str]) -> int:    
        # Pre-process arr with an optimizing helper
        # which converts each word to its character bitset
        # and then uses a set to prevent duplicate results
        opt_set = set()
        for word in arr:
            self.word_to_bitset(opt_set, word)

        # Convert the set back to an array for iteration
        # then start up the recursive helper
        opt_arr = list(opt_set)
        return self.dfs(opt_arr, 0, 0)
        
    def word_to_bitset(self, opt_arr: Set[int], word: str) -> None:        
        # Initialize an empty int to use as a character bitset
        char_bitset = 0
        for c in word:            
            # If the bitset contains a duplicate character
            # then discard this word with an early return
            # otherwise add the character to the bitset
            mask = 1 << ord(c) - 97
            if char_bitset & mask:
                return
            char_bitset += mask
        
        # Store the length of the word in the unused space
        # then add the completed bitset to our optimized set
        opt_arr.add(char_bitset + (len(word) << 26))
        
    def dfs(self, opt_arr: List[int], pos: int, res: int) -> int:        
        # Separate the parts of the bitset res
        old_chars = res & ((1 << 26) - 1)
        old_len = res >> 26
        best = old_len
        
        # Iterate through the remaining results
        for i in range(pos, len(opt_arr)):
            new_chars = opt_arr[i] & ((1 << 26) - 1)
            new_len = opt_arr[i] >> 26
            
            # If the two bitsets overlap, skip to the next result
            if new_chars & old_chars:
                continue
            
            # Combine the two results and trigger the next recursion
            new_res = new_chars + old_chars + (new_len + old_len << 26)
            best = max(best, self.dfs(opt_arr, i + 1, new_res))
        return best