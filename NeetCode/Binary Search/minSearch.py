from git import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        minNum = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                minNum = min(nums[left], minNum)
                break
            m = (left + right) // 2
            minNum = min(minNum, nums[m])
            if nums[m] >= nums[left]:
                left = m + 1
            else:
                right = m - 1

        return minNum


# Time complexity: O(log(n)) where n is the number of elements in the input array. This is because we are performing a binary search on the array, which takes O(log(n)) time.
# Space complexity: O(1) because we are using only a constant amount of extra space

#Other solution:
#Binary search lower bound
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
    
# Time complexity: O(log(n)) where n is the number of elements in the input array. This is because we are performing a binary search on the array, which takes O(log(n)) time.
# Space complexity: O(1) because we are using only a constant amount of extra space