from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return - 1

# Time complexity: O(log(n)) where n is the number of elements in the input array. This is because we are halving the search space in each iteration of the while loop.
# Space complexity: O(1) because we are using only a constant amount of extra space   

# Other solutions
# Recursive binary search: We can implement the binary search algorithm using recursion instead of iteration. The recursive approach will have the same time complexity of O(log(n)) but may have a higher space complexity due to the call stack used for recursion, which can go up to O(log(n)) in the worst case.
class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        m = l + (r - l) // 2

        if nums[m] == target:
            return m
        if nums[m] < target:
            return self.binary_search(m + 1, r, nums, target)
        return self.binary_search(l, m - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)
    
# Time complexity: O(log(n)) where n is the number of elements in the input array. This is because we are halving the search space in each recursive call of the binary search function.
# Space complexity: O(log(n)) in the worst case due to the call stack used for recursion. In the best case, when the target is found at the middle index, the space complexity would be O(1) because there would be no recursive calls.

#Upper and lower bounds: We can use the binary search algorithm to find the upper and lower bounds of the target value in the sorted array. The lower bound will give us the index of the first occurrence of the target value, while the upper bound will give us the index of the last occurrence of the target value. This approach can be useful if we want to find all occurrences of the target value in the array or if we want to count the number of occurrences of the target value in the array.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2) #we calculate the middle index m by taking the average of l and r. We use l + ((r - l) // 2) instead of (l + r) // 2 to avoid potential overflow issues when l and r are large values.
            if nums[m] > target: 
                r = m #if the middle element is greater than the target, it means that the target value must be in the left half of the current search space, so we update r to m to narrow down our search to the left half.
            elif nums[m] <= target:
                l = m + 1 #if the middle element is less than or equal to the target, it means that the target value must be in the right half of the current search space, so we update l to m + 1 to narrow down our search to the right half. We use m + 1 instead of m because we want to exclude the middle element from our search space since it has already been compared to the target value.
        return l - 1 if (l and nums[l - 1] == target) else -1
    
# Time complexity: O(log(n)) where n is the number of elements in the input array. This is because we are halving the search space in each iteration of the while loop.
# Space complexity: O(1) because we are using only a constant amount of extra space

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] >= target:
                r = m
            elif nums[m] < target:
                l = m + 1
        return l if (l < len(nums) and nums[l] == target) else -1
    
# Time complexity: O(log(n)) where n is the number of elements in the input array. This is because we are halving the search space in each iteration of the while loop.
# Space complexity: O(1) because we are using only a constant amount of extra space
#Built-in functions: We can use built-in functions in Python such as bisect_left and bisect_right from the bisect module to find the lower and upper bounds of the target value in the sorted array. These functions are optimized for performance and can provide a more concise implementation for finding the target value in the array.
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target) #the bisect_left function returns the index where the target value should be inserted in the sorted array to maintain the sorted order. If the target value is already present in the array, it returns the index of the first occurrence of the target value.
        return index if index < len(nums) and nums[index] == target else -1
    
# Time complexity: O(log(n)) where n is the number of elements in the input array. This is because the bisect_left function uses binary search to find the insertion point for the target value in the sorted array.
# Space complexity: O(1) because we are using only a constant amount of extra space