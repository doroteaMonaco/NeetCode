from collections import defaultdict


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            summ = numbers[left] + numbers[right]
            if summ > target:
                right -= 1
            elif summ  < target:
                left += 1
            else:
                return [left + 1, right + 1]
                                    
        return []

#Time complexity: O(n)
#Space complexity: O(1)

#Other solutions
#Binary search: O(nlogn) time, O(1) space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l)//2
                if numbers[mid] == tmp:
                    return [i + 1, mid + 1]
                elif numbers[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1
        return []
    
#hash map: O(n) time, O(n) space
from collections import defaultdict
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
        return []