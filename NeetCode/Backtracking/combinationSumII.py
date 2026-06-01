from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def combinations_without_repetitions(start: int, sol: List[int], candidates: List[int], target:int):
            if target == 0:
                res.append(list(sol))
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                    
                sol.append(candidates[i])
                combinations_without_repetitions(i + 1, sol, candidates, target - candidates[i])
                sol.pop()

            return
        
        sol = []
        combinations_without_repetitions(0, sol, candidates, target)
        return res

#Time complexity: O(n * 2^n) where n is the number of candidates. This is because in the worst case, we can have 2^n combinations when the target is large and the candidates are small, and generating each combination takes O(n) time in the worst case.
#Space complexity: O(n) for the recursion stack and the temporary solution list. The output list will take O(2^n) space in the worst case, but we typically don't count the output space when analyzing space complexity.
