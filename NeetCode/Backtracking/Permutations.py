from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        mark = [False] * len(nums)

        def permutations(sol: List[int], nums: List[int], mark: List[bool], n: int):
            if len(sol) == n:
                res.append(list(sol))
                return

            for i in range(n):
                if not mark[i]:
                    mark[i] = True
                    sol.append(nums[i])
                    permutations(sol, nums, mark, n)
                    sol.pop()
                    mark[i] = False
            return 

        permutations([], nums, mark, len(nums))
        return res

#Time complexity: O(n * n!)
#Space complexity: O(n) for the recursion stack and O(n) for the mark array, resulting in O(n) overall.
