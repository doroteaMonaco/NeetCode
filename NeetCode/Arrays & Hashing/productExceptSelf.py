from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []

        l = len(nums)
        pref = [0] * l
        suff = [0] * l
        res = [0] * l

        pref[0] =  1
        suff[l - 1] = 1

        for i in range(1, l):
            pref[i] = pref[i - 1] * nums[i - 1]
        
        for i in range(l - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]

        for i in range(l):
            res[i] = pref[i] * suff[i]

        return res

#Time complexity: O(n) because we iterate through the input array and the prefix and suffix arrays. The space complexity is O(n) because we store the prefix and suffix products in separate arrays, as well as the result array.
#Other solutions
#Division: we can calculate the product of all the elements in the input array and then divide the product by each element to get the result. However, this solution is not optimal because it does not handle the case where there are zeros in the input array, and it also has a time complexity of O(n) due to the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        if zero_cnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zero_cnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res
    
#Time complexity: O(n) because we iterate through the input array twice, once to calculate the product and count the zeros, and once to calculate the result. The space complexity is O(1) because we only use a constant amount of extra space to store the product and the zero count, and we modify the input array in place to store the result.
            