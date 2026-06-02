from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def powerset(sol, nums, start, n):
            res.append(list(sol))

            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                sol.append(nums[i])
                powerset(sol, nums, i + 1, n)
                sol.pop()
            
        powerset([], nums, 0, len(nums))
        return res
    
#Time complexity: O(n * 2^n) where n is the length of the input list. This is because there are 2^n subsets and generating each subset takes O(n) time in the worst case.
#Space complexity: O(n) for the recursion stack and the temporary solution list. The output list will take O(2^n) space in the worst case, but we typically don't count the output space when analyzing space complexity.