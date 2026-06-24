class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        island = 0
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]


        def bfs(r, c, island, rows, columns, grid, dirs):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))
            while q:
                i, j = q.popleft()
                for d1, d2 in dirs:
                    i1 = d1 + i
                    j1 = d2 + j
                    if (i1 < 0 or i1 >= rows or j1 < 0 or j1 >= columns or grid[i1][j1] == "0"):
                        continue
                    q.append((i1, j1))
                    grid[i1][j1] = "0"
            
            return

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":
                    bfs(i, j, island, rows, columns, grid, dirs)
                    island += 1
        
        return island

#Time complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid. This is because we visit each cell in the grid once.
#Space complexity: O(min(m, n)) for the queue used in BFS. In the worst case, the queue can hold all the cells in a row or column, which is min(m, n).

#Other solutions
#DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands