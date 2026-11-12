class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        num_of_islands = 0
        
        def dfs(row, col):

            # stop if outside grid
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            # stop if this is water or already visited
            if grid[row][col] != "1":
                return  
            
            # mark this land as visited
            grid[row][col] = "0"

            # visit neighbours
            dfs(row + 1, col)  # down
            dfs(row - 1, col)  # up
            dfs(row, col - 1)  # left
            dfs(row, col + 1)  # right

        # check every cell
        for row in range(rows):
            for col in range(cols):

                # found a new island
                if grid[row][col] == "1":
                    num_of_islands += 1

                    # visit the whole island
                    dfs(row, col)

        return num_of_islands

        