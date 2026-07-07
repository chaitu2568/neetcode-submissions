class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows,cols = len(grid),len(grid[0])
        count = 0
        def dfs(row,col):
            grid[row][col] = "0"
            for nr,nc in [(row+1,col),(row-1,col),(row,col+1),(row,col-1)]:
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == "1":
                    dfs(nr,nc)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row,col)
                    count += 1
        
        return count
        
        