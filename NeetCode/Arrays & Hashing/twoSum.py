from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, num in enumerate(nums):
            map[num] = index
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map and (map[diff] != i):
                return [i, map[diff]]
            
        return 

#Other solutions
#Sorting: we can sort the array and use two pointers to find the two numbers taht sum up to teh target.
#The time complexity of this solution is O(nlogn) because of the sorting step, and the space complexity is O(1) if we sort the array in place, or O(n) if we create a new sorted array.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])

        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []
    
#Hash Map One pass: by iterating through the array and checking if teh complement of teh current element exists in the hash map
#if it does we return the indices, otherwise we store teh current element in teh hash map.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i