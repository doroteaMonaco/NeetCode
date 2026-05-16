
from ast import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while True: # Find the intersection point in the cycle
            slow = nums[slow] # Move slow by 1 step
            fast = nums[nums[fast]] # Move fast by 2 steps
            if slow == fast:
                break

        slow = 0 # Find the entrance to the cycle
        while slow != fast: # Move both slow and fast by 1 step until they meet at the entrance of the cycle
            slow = nums[slow]
            fast = nums[fast]

        return slow

# Time complexity: O(n) where n is the number of elements in the input list
# Space complexity: O(1) since we are using only a constant amount of extra space
# Other solution: using the input list itself to mark visited numbers by negating the value at the index corresponding to the number
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums :
            idx = abs(num) - 1 # Get the index corresponding to the number (subtract 1 to account for 0-based indexing)
            if nums[idx] < 0 : # If the value at that index is already negative, it means we have seen this number before, so we return the absolute value of the number as the duplicate
                return abs(num)
            nums[idx] *= -1
        return -1

# Time complexity: O(n) where n is the number of elements in the input list
# Space complexity: O(1) since we are using only a constant amount of extra space

#Bit manipulation

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for b in range(32): # Iterate through each bit position from 0 to 31 (assuming 32-bit integers)
            x = y = 0 
            mask = 1 << b # Create a mask with only the b-th bit set to 1 (e.g., if b=0, mask=1; if b=1, mask=2; if b=2, mask=4; etc.)
            for num in nums:
                if num & mask: # If the b-th bit of the number is set to 1, increment x
                    x += 1

            for num in range(1, n):
                if num & mask: # If the b-th bit of the number is set to 1, increment y
                    y += 1

            if x > y:
                res |= mask # If the count of numbers with the b-th bit set to 1 in the input list is greater than the count of numbers with the b-th bit set to 1 in the range from 1 to n-1, it means that the duplicate number has the b-th bit set to 1, so we set that bit in the result using a bitwise OR operation.
        return res
    
#Explanation
#The list is composed of n + 1 integers where each integer is in the range [1, n] inclusive.
# It reconstructs the duplicate number bit by bit.
#So first step, we iterate through each bit position from 0 to 31 (assuming 32-bit integers). 
#For each bit position, we count how many numbers in the input list have that bit set to 1 (stored in x)
# and how many numbers from 1 to n-1 have that bit set to 1 (stored in y).\
# if the count of the b-th bit in the input list is greater than the count of the b-th bit in the range from 1 to n-1,
# it means that the duplicate number has the b-th bit set to 1, so we set that bit in the result using a bitwise OR operation.
