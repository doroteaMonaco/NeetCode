from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]: # if the middle element is greater than the rightmost element, it means that the minimum element is in the right half of the array. Therefore, we can move the left pointer to m + 1 to search for the minimum element in the right half.
                l = m + 1
            else:
                r = m

        pivot = l
        l, r = 0, len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]: # if the target is greater than or equal to the minimum element and less than or equal to the rightmost element, it means that the target is in the right half of the array. Therefore, we can move the left pointer to pivot to search for the target in the right half.
            l = pivot
        else:
            r = pivot - 1

        while l <= r: # we perform a standard binary search on the selected half of the array to find the target element. We calculate the middle index m and compare the middle element with the target. If they are equal, we return the index m. If the middle element is less than the target, it means that the target is in the right half of the selected range, so we move the left pointer to m + 1. Otherwise, if the middle element is greater than the target, it means that the target is in the left half of the selected range, so we move the right pointer to m - 1.
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

# Time complexity: O(log(n)) where n is the number of elements in the input array. This is because we are performing a binary search on the array, which takes O(log(n)) time.
# Space complexity: O(1) because we are using only a constant amount of extra space

# Other solution:
# Binary search lower bound

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        return binary_search(pivot, len(nums) - 1)
    
# Time complexity: O(log(n)) where n is the number of elements in the input array. This is because we are performing a binary search on the array, which takes O(log(n)) time.
# Space complexity: O(1) because we are using only a constant amount of extra space

#Binary search one pass

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
    
# Time complexity: O(log(n)) where n is the number of elements in the input array. This is because we are performing a binary search on the array, which takes O(log(n)) time.
# Space complexity: O(1) because we are using only a constant amount of extra space