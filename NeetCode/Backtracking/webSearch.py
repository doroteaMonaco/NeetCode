from git import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def backtracking(board: List[List[str]], visited: List[List[bool]], r: int, c: int, index: int, word: str, rows: int, cols: int):
            if index == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] == True or board[r][c] != word[index]:
                return False
            
            visited[r][c] = True
            res = (backtracking(board, visited, r + 1, c, index + 1, word, rows, cols) or
            backtracking(board, visited, r - 1, c, index + 1, word, rows, cols) or
            backtracking(board, visited, r, c + 1, index + 1, word, rows, cols) or
            backtracking(board, visited, r, c - 1, index + 1, word, rows, cols))
            visited[r][c] = False
            return res
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and backtracking(board, visited, i, j, 0, word, rows, cols):
                    return True
        return False

#Time complexity: O(m * 4^n) where m is the number of cells in the board and n is the length of the word. This is because in the worst case, we might have to explore all possible paths for each cell in the board.
#Space complexity: O(n) for the recursion stack and the visited matrix. The visited matrix takes O(m) space, but we typically don't count the output space when analyzing space complexity.

