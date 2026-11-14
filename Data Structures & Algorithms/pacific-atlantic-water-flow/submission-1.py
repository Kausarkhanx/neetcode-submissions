class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        # cells that can reach each ocean
        pacific = set()
        atlantic = set()

        def dfs(row, col, visited, previous_height):

            # outside grid
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            # already visited this cell
            if (row, col) in visited:
                return None

            # current cell is too low
            # remember: we are travelling BACKWARDS from the ocean
            if heights[row][col] < previous_height:
                return

            # mark this cell as visited
            visited.add((row, col))

            # current height
            current_height = heights[row][col]

            # explore 4 directions
            dfs(row + 1, col, visited, current_height)  # down
            dfs(row - 1, col, visited, current_height)  # up
            dfs(row, col - 1, visited, current_height)  # left
            dfs(row, col + 1, visited, current_height)  # right

        # TOP and BOTTOM rows
        for col in range(cols):

            # top = Pacific
            dfs(0, col, pacific, heights[0][col])

            # bottom = Atlantic
            dfs(rows - 1, col, atlantic, heights[rows - 1][col])

        # LEFT and RIGHT columns
        for row in range(rows):

            # left = Pacific
            dfs(row, 0, pacific, heights[row][0])

            # right = Atlantic
            dfs(row, cols - 1, atlantic, heights[row][cols - 1])

        result = []

        # cells that can reach BOTH oceans
        for row in range(rows):
            for col in range(cols):

                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result