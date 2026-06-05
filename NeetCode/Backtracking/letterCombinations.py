from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.digits = digits
        
        if not self.digits:
            return []
            
        self.num_letters = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        res = []
        
        def backtracking(index: int, sol: str):
            if len(sol) == len(self.digits):
                res.append(sol)
                return
            
            letters = self.num_letters[self.digits[index]]

            for l in letters:
                backtracking(index + 1, sol + l)

            return

        backtracking(0, "")
        return res

#Time complexity: O(4^n * n) where n is the length of the input digits string. This is because in the worst case, each digit can map to 4 letters (like '7' and '9'), leading to 4^n combinations.
#Space complexity: O(n) for the recursion stack and the temporary solution string. The output list will take O(4^n * n) space in the worst case, but we typically don't count the output space when analyzing space complexity.