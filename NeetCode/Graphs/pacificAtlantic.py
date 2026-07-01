from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, ocean, h):  #save the height of the previous recursion to make a comparison
            if (r, c) in ocean or r < 0 or c < 0 or r >= R or c >= C or heights[r][c] < h:
                return
            
            ocean.add((r, c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])


        for c in range(C):
            dfs(0, c, pacific, heights[0][c])
            dfs(R - 1, c, atlantic, heights[R - 1][c])

        for r in range(R):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, C - 1, atlantic, heights[r][C - 1])
        
        result = pacific.intersection(atlantic)
        return list(result)

#Time complexity: O(m * n)
#Space complexity: O(m * n)

#Other solutions

#BFS
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False] * COLS for _ in range(ROWS)] #mask for each couple of coordinates
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions: #explore all the possible directions
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))

        pacific = [] #save the coordinates of the cells of the oceans
        atlantic = []
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]: #intersection of the oceans where masks are True
                    res.append([r, c])
        return res
