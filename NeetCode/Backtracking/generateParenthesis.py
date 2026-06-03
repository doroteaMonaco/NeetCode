from git import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(sol: List, n: int, openP: int, closedP: int, l: int):
            if len(sol) == l:
                string = "".join(sol)
                res.append(string)
                return
            
            if openP < n:
                sol.append("(")
                backtracking(sol, n, openP + 1, closedP, l)
                sol.pop()
            if closedP < openP:
                sol.append(")")
                backtracking(sol, n, openP, closedP + 1, l)
                sol.pop()
            
            return


        backtracking([], n, 0, 0, n*2)
        return res

#Time complexity: O(4^n / sqrt(n)) which is the number of valid combinations of parentheses. This is because the number of valid combinations of parentheses is given by the nth Catalan number, which can be approximated as C(n) ~ 4^n / (n^(3/2) * sqrt(pi)).
#Space complexity: O(n) for the recursion stack and the temporary solution list. The output list will take O(4^n / sqrt(n)) space in the worst case, but we typically don't count the output space when analyzing space complexity.

