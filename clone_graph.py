def cloneGraph(self, node: 'Node') -> 'Node':
    # Time complexity: O(N+M), N - number of Nodes, M - number of edges
    # Space complexity: O(N), space occupied by the visited hash map and recursion stack equal to           height of the graph
    oldToNewMap = {}
    def clone(node):
        if node in oldToNewMap:
            return oldToNewMap[node]
        copy = Node(node.val)
        oldToNewMap[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(clone(nei))
        return copy
    return clone(node) if node is not None else None           

