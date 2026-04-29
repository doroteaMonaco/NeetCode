import sys
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicate = False
        map = {}

        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        
        for key in map:
            if map[key] > 1:
                hasDuplicate = True
                break
        
        return hasDuplicate

    def main():
        nums = [0, 1, 1, 9, 9, 8]
        sol = Solution()
        print(sol.hasDuplicate(nums))


# Others' solution
# 1. Sorting
# if we sorte the array, the duplicates will appear next to each other. We can then check if any adjacent elements are the same.
class Solution:
    def hasDuplicates(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
#The time complexity of this solution is O(n log n) due to the sorting step, and the space complexity is O(1) if we sort in place, or O(n) if we create a new sorted array.

#2. Hash Set

class Solution:
    def hasDuplicates(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False