class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.cols = set()
        self.diags = set()
        self.anti_diags = set()

        matrix = [["."] * n for _ in range(n)]

        def backtracking(m: List[List[str]], n: int, r: int):
            if r == n:
                sol = []
                for row in m:
                    copy = "".join(row)
                    sol.append(copy)
                res.append(sol)
                return
            
            for c in range(n):
                if c in self.cols or (r + c) in self.anti_diags or (r - c) in self.diags:
                    continue
                
                self.cols.add(c)
                self.diags.add(r - c)
                self.anti_diags.add(r + c)
                m[r][c] = "Q"

                backtracking(m, n, r + 1)

                self.cols.remove(c)
                self.diags.remove(r - c)
                self.anti_diags.remove(r + c)
                m[r][c] = "."

            return


        backtracking(matrix, n, 0)
        return res


#Time complexity: O(n!) where n is the size of the board. This is because in the worst case, we can have n choices for the first row, n-1 for the second, and so on, leading to n! combinations. Additionally, we need O(n) time to construct each solution.
#Space complexity: O(n) for the recursion stack and the temporary solution matrix. The output list will take O(n! * n) space in the worst case, but we typically don't count the output space when analyzing space complexity.