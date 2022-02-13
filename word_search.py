def exist(self, board: List[List[str]], word: str) -> bool:
    # Time complexity: O(m*n*4^len(word))
    rows, cols = len(board), len(board[0])
    wordlen = len(word)
    # using the set - path to keep track of visited locations
    path = set()
    
    # DFS function using row, col and index i of the word being checked
    def dfs(r, c, i):
        # base case
        # reached end of word
        if i==wordlen:
            return True
        
        # invalid cases
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i] or (r,c) in path:
            return False
        
        # Found valid character, add coord to path
        path.add((r,c))
        
        # Proceed in 4 directions
        res = dfs(r-1, c, i+1) or dfs(r+1, c, i+1) or dfs(r, c-1, i+1) or dfs(r, c+1, i+1)
        
        # Returned back, remove coord from path
        path.remove((r,c))
        
        return res
    
    for r in range(rows):
        for c in range(cols):
            res = dfs(r, c, 0)
            if res:
                return True
    
    return False
    