class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo, hi = 0, len(people)-1
        co = 0
        while lo<hi:
            if people[lo] + people[hi] <= limit:
                lo+=1
                hi-=1
            else:
                hi-=1
            co += 1
        if lo == hi:
            co += 1
        return co

        