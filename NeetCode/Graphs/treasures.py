from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0 # Distance from the nearest treasure
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist # Update the cell with the distance from the nearest treasure
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1

#Time complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid. This is because we visit each cell in the grid once.
#Space complexity: O(m * n) for the queue used in BFS. In the worst case, the queue can hold all the cells in the grid.

#Other solutions
#DFS
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c, dist):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            grid[r][c] = dist # Update the cell with the distance from the nearest treasure
            dfs(r + 1, c, dist + 1)
            dfs(r - 1, c, dist + 1)
            dfs(r, c + 1, dist + 1)
            dfs(r, c - 1, dist + 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(r, c, 0)

#Time complexity: O(m * n) where m is the number of rows and n is the number of columns in the grid. This is because we visit each cell in the grid once.
#Space complexity: O(m * n) for the recursive call stack. In the worst case, the recursion stack can hold all the cells in the grid, which is m * n.
