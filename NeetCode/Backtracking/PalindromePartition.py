from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(s: List[str]):
            if not s:
                return False
            return s == s[::-1]

        def backtracking(s: str, start: int, sol: List[str]):
            if start == len(s):
                res.append(list(sol))
                return

            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]

                if isPalindrome(sub):
                    sol.append(sub)
                    backtracking(s, end, sol)
                    sol.pop()

            return
            
        backtracking(s, 0, [])
        return res
    
#Time complexity: O(n * 2^n) where n is the length of the input string. This is because there are 2^n possible partitions and checking if each partition is a palindrome takes O(n) time in the worst case.
#Space complexity: O(n) for the recursion stack and the temporary solution list. The output list will take O(2^n) space in the worst case, but we typically don't count the output space when analyzing space complexity.
