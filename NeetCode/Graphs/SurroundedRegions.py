from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])

        def dfs(r, c):
            nonlocal R, C
            if r < 0 or c < 0 or r >= R or c >= C or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        for r in range(R):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][C - 1] == 'O':
                dfs(r, C - 1)

        for c in range(C):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[R - 1][c] == 'O':
                dfs(R - 1, c)
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'

#Time complexity: O(m * n)
#Space complexity: O(m * n)

#Other solutions
#BFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def capture():
            q = deque()
            for r in range(ROWS):
                for c in range(COLS):
                    if (r == 0 or r == ROWS - 1 or
                        c == 0 or c == COLS - 1) and board[r][c] == "O":
                        q.append((r, c))
            while q:
                r, c = q.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS:
                            q.append((nr, nc))

        capture()
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

#Time complexity: O(m * n)
#Space complexity: O(m * n)