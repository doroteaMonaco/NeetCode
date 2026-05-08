
from typing import List


class Solution:
    def hoursRequired(self, piles: List[int], k: int) -> int:
        hours = 0

        for bananas in piles:
            if bananas <= k:
                hours += 1
            else:
                hours += (bananas + k - 1) // k

        return hours



    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        k_min = max(piles)

        while left <= right:
            m = (left + right) // 2

            hours = self.hoursRequired(piles, m)
            if hours > h:
                left = m + 1
            else:
                k_min = min(k_min, m)
                right = m - 1
        
        return k_min

# Time complexity: O(n log(m)) where n is the number of piles and m is the maximum number of bananas in any pile. This is because we are performing a binary search on the range of possible eating speeds, which takes O(log(m)) time, and for each eating speed, we are calculating the total hours required to eat all the bananas, which takes O(n) time.
# Space complexity: O(1) because we are using only a constant amount of extra space
