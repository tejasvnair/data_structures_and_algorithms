def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    preReqMap = {i:[] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preReqMap[crs].append(pre)
    visitSet = set()
    
    def dfs(crs):
        # base cases
        # the course has been visited so its cyclic (can't be completed)
        if crs in visitSet:
            return False
        # No pre-req, course can be completed
        if preReqMap[crs] == []:
            return True
        
        visitSet.add(crs)
        for pre in preReqMap[crs]:
            if not dfs(pre):
                return False
        # crs can be completed, so set pre-reqs to empty
        preReqMap[crs] = []
        visitSet.remove(crs)
        return True
    
    for i in range(numCourses):
        if not dfs(i):
            return False
    
    return True
        
