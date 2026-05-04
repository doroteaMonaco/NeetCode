

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxA = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            maxA = max(area, maxA)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
           

        return maxA
#Time complexity: O(n)
#Space complexity: O(1)

#Other solutions
#Brute force: O(n^2) time, O(1) space
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                area = min(heights[i], heights[j]) * (j - i)
                maxA = max(area, maxA)
        return maxA
    
#Time complexity: O(n^2)
#Space complexity: O(1)
