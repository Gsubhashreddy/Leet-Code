import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused , used = list(range(n)), []
        count = [0 for i in range(n)]
        heapq.heapify(unused)
        for i in sorted(meetings):
            start, end = i[0] , i[1]
            while used and used[0][0] <=start:
                room = heapq.heappop(used)
                heapq.heappush(unused, room[1])
            if unused:
                room = heapq.heappop(unused)
                heapq.heappush(used, [end, room])
                count[room] +=1
            else:
                room = heapq.heappop(used)
                heapq.heappush(used, [room[0] + end- start, room[1]])
                count[room[1]]+=1
        return count.index(max(count))
                
            
            
        