class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftmax, rightmax = height[left], height[right]
        water = 0
        
        while left < right:
            if leftmax < rightmax:
                left += 1
                leftmax = max(height[left], leftmax)
                tmp = (leftmax - height[left])
                water += tmp
            else:
                right -= 1
                rightmax = max(rightmax, height[right])
                tmp = (rightmax - height[right])
                water += tmp

        return water
#Time complexity: O(n)
#Space complexity: O(1)

#Other solutions
#Prefix and Suffix arrays
#fill leftMax and rightMax arrays with the maximum height to the left and to the right of each position, then calculate the water trapped at each position as min(leftMax[i], rightMax[i]) - height[i]

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        leftMax = [0] * n
        rightMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res
#Time complexity: O(n)
#Space complexity: O(n)

#Stack
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        stack = []
        res = 0

        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]: #while the current height is greater than the height of the top of the stack
                mid = height[stack.pop()] #the height of the middle bar
                if stack:
                    right = height[i] #the height of the right bar
                    left = height[stack[-1]] #the height of the left bar
                    h = min(right, left) - mid #the height of the trapped water
                    w = i - stack[-1] - 1 #the width of the trapped water
                    res += h * w
            stack.append(i)
        return res
#Time complexity: O(n)
#Space complexity: O(n)