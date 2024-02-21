class Solution:
    visited, completed, depe = {}, {}, {}
    
    def isFinished(self, course):
        if course in self.completed or course not in self.depe:
            self.completed[course] = True
            return True
        if course in self.visited:
            return False
        self.visited[course] = True
        for sub in self.depe[course]:
            res = self.isFinished(sub)
            if not res:
                return False
            self.completed[sub] = True
        self.completed[course] = True
        return True
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.depe = {}
        for course in prerequisites:
            if course[0] in self.depe:
                temp = self.depe[course[0]]
                temp.append(course[1])
                self.depe[course[0]] = temp
            else:
                self.depe[course[0]] = [course[1]]
        
        # Now go through all depe
        # For each you should have visited and global completed
        print(self.depe)
        self.completed = {}
        for co in self.depe:
            self.visited = {}
            res = self.isFinished(co)
            if not res:
                return False
                # Do the following
            self.completed[co] = True
            
        return True
        