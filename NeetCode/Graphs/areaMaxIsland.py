from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        maxArea = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(grid, R, C, r, c, dirs):
            area = 0
            q = deque()
            q.append((r,c))
            area += grid[r][c]
            grid[r][c] = 0

            while q:
                r1, c1 = q.popleft()
                for nr, nc in dirs:
                    rf = r1 + nr
                    cf = c1 + nc
                    if rf < 0 or cf < 0 or rf >= R or cf >= C or grid[rf][cf] == 0:
                        continue
                    
                    q.append((rf, cf))
                    area += grid[rf][cf]
                    grid[rf][cf] = 0

            return area


        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    area = bfs(grid, R, C, i, j, dirs)
                    maxArea = max(maxArea, area)
        
        return maxArea

#Time complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid. This is because we visit each cell in the grid once.
#Space complexity: O(min(m, n)) for the queue used in BFS. In the worst case, the queue can hold all the cells in a row or column, which is min(m, n).

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        maxArea = 0
        visit = set()

        def dfs(grid, R, C, r, c, visit):
            if r < 0 or c < 0 or r == R or c == C or grid[r][c] == 0 or (r,c) in visit:
                return 0
            
            visit.add((r,c))
            return (1 + dfs(grid, R, C, r, c + 1, visit) + dfs(grid, R, C, r, c - 1, visit) + dfs(grid, R, C, r + 1, c, visit) + dfs(grid, R, C, r - 1, c, visit))


        for i in range(R):
            for j in range(C):
                area = dfs(grid, R, C, i, j, visit)
                maxArea = max(maxArea, area)
        
        return maxArea
    
#Time complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid. This is because we visit each cell in the grid once.
#Space complexity: O(m * n) for the recursion stack in DFS. In the worst case, the recursion stack can hold all the cells in the grid, which is m * n.