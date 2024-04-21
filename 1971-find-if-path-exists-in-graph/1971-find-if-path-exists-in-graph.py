class Solution:
    flag = False
    def dfs(self,maps, curr, visi, target):
        if curr == target:
            self.flag = True
            return
        if curr in visi:
            return
        visi[curr] = True
        for des in maps.get(curr,[]):
            self.dfs(maps,des,visi, target)
            if self.flag:
                return
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        maps = {}
        visi= {}
        self.flag = False
        for edge in edges:
            x,y = edge[0], edge[1]
            if x in maps:
                maps[x].append(y)
            else:
                maps[x] = [y]
            if y in maps:
                maps[y].append(x)
            else:
                maps[y] = [x]
        if len(maps.get(source,[])) == 0:
            return False
        visi[source] = True
        for des in maps[source]:
            self.dfs(maps,des,visi, destination)
        print(maps)
        return self.flag
        
        