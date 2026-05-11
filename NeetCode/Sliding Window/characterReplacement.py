
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        maxLength = 0
        maxChar = 0
        charMap = defaultdict(int)


        for right in range(len(s)):
            charMap[s[right]] += 1
            
            maxChar = max(maxChar, charMap[s[right]])
            while ((right - left + 1) - maxChar) > k: # if the number of characters that need to be replaced (which is the total length of the current window minus the count of the most frequent character) is greater than k, it means that we cannot replace all the characters in the current window to make them the same. Therefore, we need to shrink the window from the left until we have at most k characters that need to be replaced.
                charMap[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength

# Time complexity: O(n) where n is the length of the input string. This is because we are iterating through the string once with two pointers, which takes O(n) time.
# Space complexity: O(1) because we are using a fixed-size dictionary to store the count of characters in the current window, and the size of the dictionary can be at most the size of the character set, which is constant.

# Other solution:
#Sliding window with a set to store the unique characters in the current window
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res
    
# Time complexity: O(n * m) where n is the length of the input string and m is the size of the character set. This is because we are iterating through the string once for each unique character in the character set, which takes O(n) time for each character, resulting in a total time complexity of O(n * m).
# Space complexity: O(m) where m is the size of the character set. This is because we are using a set to store the unique characters in the current window, and the size of the set can be at most the size of the character set.       