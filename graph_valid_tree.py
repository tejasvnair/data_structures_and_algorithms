def validTree(self, n: int, edges: List[List[int]]) -> bool:
    # Time complexity: O(n+k)
    # Space complexity: O(n+k)
    # Conditions for a graph to be valid tree:
    # - All nodes should be connected to atleast 1 node
    # - There shouldn't be any loop
    
    # use visit set to track number of nodes visited and loops
    visit = set()
    adj = {i:[] for i in range(n)}
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
    
    def dfs(node, prev):
        # Detected a loop - base return case
        if node in visit:
            return False
        
        visit.add(node)
        
        for nei in adj[node]:
            if nei==prev:
                continue
            if not dfs(nei, node):
                return False
        return True
    
    has_no_loop = dfs(0, -1)
    num_visited_nodes = len(visit)
    is_conn = (num_visited_nodes == n)
    
    return has_no_loop and is_conn
    
