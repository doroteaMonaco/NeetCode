from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def combinations_rip(start: int, target: int, sol: List[int], nums: List[int]):
            if target == 0:
                res.append(list(sol)) #copy the current solution to the result list
                return
            if target < 0:
                return 

            for i in range(start, len(nums)):
                sol.append(nums[i])
                combinations_rip(i, target - nums[i], sol, nums)
                sol.pop()

            return 
        sol = []
        combinations_rip(0, target, sol, nums)
        return res
    
#Time complexity: O(k * n^k) where k is the average length of the combinations and n is the number of candidates. This is because in the worst case, we can have k levels of recursion and at each level, we iterate through n candidates.
#Space complexity: O(k) for the recursion stack and the temporary solution list. The output list will take O(n^k) space in the worst case, but we typically don't count the output space when analyzing space complexity.

#Other solution
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()

        dfs(0, [], 0)
        return res
#Time complexity: O(2^mt) where m is the number of candidates and t is the target value. This is because in the worst case, we can have 2^t combinations when the target is large and the candidates are small.
#Space complexity: O(mt) for the recursion stack and the temporary solution list. The output list will take O(2^t) space in the worst case, but we typically don't count the output space when analyzing space complexity.