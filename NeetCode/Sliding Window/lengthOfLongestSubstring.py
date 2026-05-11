class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        chars = set()
        l = 0
        maxLength = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            maxLength = max(maxLength, r - l + 1)

        return maxLength

        
# Time complexity: O(n) where n is the length of the input string. This is because we are iterating through the string once with two pointers, which takes O(n) time.
# Space complexity: O(min(m, n)) where m is the size of the character set and n is the length of the input string. This is because we are using a set to store the unique characters in the current window, and the size of the set can be at most the size of the character set or the length of the input string, whichever is smaller.       

#Other solution:
# Sliding window with a dictionary to store the last index of each character
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l) # if the current character is already in the dictionary, it means that we have found a repeating character. We need to move the left pointer to the right of the last index of the current character to ensure that we are only considering unique characters in the current window. We take the maximum of mp[s[r]] + 1 and l to ensure that we do not move the left pointer backwards, which could happen if there are multiple occurrences of the same character in the string.
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res

# Time complexity: O(n) where n is the length of the input string. This is because we are iterating through the string once with two pointers, which takes O(n) time.
# Space complexity: O(min(m, n)) where m is the size of the character set and n is the length of the input string. This is because we are using a dictionary to store the last index of each character, and the size of the dictionary can be at most the size of the character set or the length of the input string, whichever is smaller.