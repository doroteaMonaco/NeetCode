class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maxArray = []
        left = 0
        window = []

        for i in range(left, left + k):
            window.append(nums[i])

        maxArray.append(max(window))

        for j in range(0, len(nums) - k):
            window.remove(nums[j])
            window.append(nums[j + k])
            maxArray.append(max(window))

        return maxArray

# Time complexity: O(n * k) where n is the length of the input array and k is the size of the sliding window. This is because we are iterating through the input array once, and for each element in the array, we are calculating the maximum value in the current window, which takes O(k) time.
# Space complexity: O(k) because we are using a list to store the elements in the current window, and the size of the list can be at most k. We are also using a list to store the maximum values for each window, but the size of this list can be at most n - k + 1, which is less than or equal to n. Therefore, the overall space complexity is O(k).

#Other solution:
# Sliding window with a deque to store the indices of the elements in the current window

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # we are iterating through the input array with a right pointer r, and for each element in the array, we are checking if the current element is greater than the last element in the deque. If it is, it means that the current element is greater than all the elements in the current window that are smaller than it, and we can remove those elements from the deque because they will never be the maximum value in any future window. We continue to remove elements from the deque until we find an element that is greater than or equal to the current element, or until the deque is empty. After that, we add the index of the current element to the deque.
                q.pop()
            q.append(r)

            if l > q[0]: # if the left pointer is greater than the index of the maximum value in the current window (which is the first element in the deque), it means that the maximum value is no longer in the current window, and we can remove it from the deque.
                q.popleft()

            if (r + 1) >= k: # if the right pointer is greater than or equal to k - 1, it means that we have reached the end of the first window, and we can start adding the maximum values for each window to the output list. The maximum value for the current window is the element at the index of the first element in the deque, which is nums[q[0]]. We add this value to the output list, and then we move the left pointer to the right by one to start checking the next window.
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

# Time complexity: O(n) where n is the length of the input array. This is because we are iterating through the input array once with a right pointer, and for each element in the array, we are adding and removing elements from the deque at most once, which takes O(1) time. Therefore, the overall time complexity is O(n).
# Space complexity: O(k) because we are using a deque to store the indices of the elements in the current window, and the size of the deque can be at most k. We are also using a list to store the maximum values for each window, but the size of this list can be at most n - k + 1, which is less than or equal to n. Therefore, the overall space complexity is O(k).