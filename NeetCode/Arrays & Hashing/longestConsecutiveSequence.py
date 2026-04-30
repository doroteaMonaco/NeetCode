


from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for num in nums:
            if num not in seen:
                seen.add(num)

        for num in seen:
            if (num - 1) not in seen:
                length = 1
                while (num + length) in seen:
                    length += 1
                longest = max(length, longest)
        return longest

#Time complexity: O(n) because we iterate through the input array and the seen set. The space complexity is O(n) because we store the unique numbers in a set.
#Other solutions
#Sorting: we can sort the input array and then iterate through it to find the longest consecutive sequence. The time complexity of this solution is O(nlogn) because of the sorting step, and the space complexity is O(1) if we sort the array in place, or O(n) if we create a new sorted array.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        nums.sort()

        curr, streak = nums[0], 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        return res
    
#Time complexity: O(nlogn) because of the sorting step, and the space complexity is O(1) if we sort the array in place, or O(n) if we create a new sorted array.

#Hash Map: we can use a hash map to store the length of the longest consecutive sequence that ends with each number in the input array. We iterate through the input array and for each number, we check if it is the start of a new sequence (i.e., if the previous number is not in the hash map). If it is, we calculate the length of the sequence by checking how many consecutive numbers are in the hash map starting from the current number. We then update the longest sequence length if necessary.
#each position in the hash map represents the length of the longest consecutive sequence that ends with that number. The time complexity of this solution is O(n) because we iterate through the input array and the hash map, and the space complexity is O(n) because we store the length of the longest consecutive sequence for each number in the hash map.
#the left boundary of the sequence is the current number minus the length of the sequence, and the right boundary is the current number plus the length of the sequence. We can then update the length of the sequence for both boundaries in the hash map to be the length of the current sequence.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                mp[num - mp[num - 1]] = mp[num]
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res
    
#Time complexity: O(n) because we iterate through the input array and the hash map, and the space complexity is O(n) because we store the length of the longest consecutive sequence for each number in the hash map.
        
                

        
            
            