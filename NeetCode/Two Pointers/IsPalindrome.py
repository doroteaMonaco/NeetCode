class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        s = s.lower()
        for c in s:
            if c.isalnum() and not c.isspace():
                new_s += c
        
        left, right = 0, len(new_s) - 1
        
        while left < right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1

        return True