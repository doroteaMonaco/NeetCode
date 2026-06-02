from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = [0] * len(nums)
        def powerset_bitmask(nums, pos, sol, n):
            if pos == n:
                powerset = [nums[i] for i in range(n) if sol[i] == 1]
                res.append(powerset)
                return 1


            sol[pos] = 0
            count = powerset_bitmask(nums, pos + 1, sol, n)
            sol[pos] = 1
            count += powerset_bitmask(nums, pos + 1, sol, n)
            

            return count
        powerset_bitmask(nums, 0, sol, len(nums))
        return res

#Time complexity: O(n * 2^n) where n is the length of the input list. This is because there are 2^n subsets and generating each subset takes O(n) time in the worst case.
#Space complexity: O(n) for the recursion stack and the temporary solution list. The output list will take O(2^n) space in the worst case, but we typically don't count the output space when analyzing space complexity.

