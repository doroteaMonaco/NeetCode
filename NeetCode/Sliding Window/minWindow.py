class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        map = {}
        minLength = float("inf")
        res = [-1, -1]

        for char in t:
            map[char] = map.get(char, 0) + 1

        left = 0
        need = len(map)
        window = {}
        have = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if window[s[right]] == map.get(s[right], 0):
                have += 1
            while have == need:
                if (right - left + 1) < minLength:
                    res = [left, right]
                    minLength = right - left + 1
                window[s[left]] -= 1
                if s[left] in map and window[s[left]] < map[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        if minLength != float("inf"):
            return s[l:r + 1]
        
        return ""

# Time complexity: O(n + m) where n is the length of the input string s and m is the length of the input string t. This is because we are iterating through both strings once to create the character count map for t and to find the minimum window in s, which takes O(n + m) time.
# Space complexity: O(m) where m is the length of the input string t. This is because we are using a dictionary to store the count of characters in t, and the size of the dictionary can be at most the length of t. We are also using a dictionary to store the count of characters in the current window of s, but the size of this dictionary can be at most the size of the character set, which is constant. Therefore, the overall space complexity is O(m).
