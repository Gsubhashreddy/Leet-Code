import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        # First use all ladders, and create min heap
        # Then while using bricks, check if the length is greater than bricks
        # If yes, replace bricks with that
        heaps = []
        count = 1
        for i in range(len(heights)-1):

            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue
            heapq.heappush(heaps, diff)
            # If we haven't gone over the number of ladders, nothing else to do.
            if len(heaps) <= ladders:
                continue
            bricks -= heapq.heappop(heaps)
            if bricks < 0:
                return i
        return len(heights) - 1
            
                    
                