from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nc >= 0 and nr < R and nc < C and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
        
#Time complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid. This is because we visit each cell in the grid once.
#Space complexity: O(m * n) for the queue used in BFS. In the worst case, the queue can hold all the cells in the grid.

