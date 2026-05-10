
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        maxProfit = 0


        for i in range(len(prices)):
            j = len(prices) - 1
            while j > i:
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                    maxProfit = max(profit, maxProfit)
                j -= 1
        
        return maxProfit
    
# Time complexity: O(n^2) where n is the number of elements in the input array. This is because we have two nested loops, where the outer loop iterates through each element and the inner loop iterates through the remaining elements to calculate the profit.
# Space complexity: O(1) because we are using only a constant amount of extra space

#Other solution:
# Two pointers solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

# Time complexity: O(n) where n is the number of elements in the input array. This is because we are iterating through the array once with two pointers, which takes O(n) time.
# Space complexity: O(1) because we are using only a constant amount of extra space

#Dynamic programming solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP

# Time complexity: O(n) where n is the number of elements in the input array. This is because we are iterating through the array once, which takes O(n) time.
# Space complexity: O(1) because we are using only a constant amount of extra space