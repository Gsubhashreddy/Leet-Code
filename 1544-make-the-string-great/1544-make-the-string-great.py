class Solution:
    def makeGood(self, s: str) -> str:
        # Use stack to store the visited characters.
        stack = []
        
        # Iterate over 's'.
        for curr_char in list(s):
            if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(curr_char)
        return "".join(stack)