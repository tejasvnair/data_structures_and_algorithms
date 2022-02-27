class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Time complexity: O(n*m)
        # Space complexity: O(n*m)
        pac = set() # set of grid cells reachable from pacific ocean
        atl = set() # set of grid cells reachable from atlantic ocean
        ROWS, COLS = len(heights), len(heights[0])
        
        def dfs(r, c, ocnset, h):
            # find cells which are reachable
            
            # base cases - return if out of bounds or cells are not reachable
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in ocnset or heights[r][c] < h:
                return
            
            # cell is reachable
            ocnset.add((r, c))
            dfs(r-1, c, ocnset, heights[r][c]) # Go Top
            dfs(r+1, c, ocnset, heights[r][c]) # Go Bottom
            dfs(r, c-1, ocnset, heights[r][c]) # Go Left
            dfs(r, c+1, ocnset, heights[r][c]) # Go Right
            return            
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # start from top row
            dfs(ROWS-1, c, atl, heights[ROWS-1][c]) # start from bottom row
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) # start from left column
            dfs(r, COLS-1, atl, heights[r][COLS-1]) # start from right column
        
        # return common cells between grids reachable from pac and atl
        return pac & atl
        
        