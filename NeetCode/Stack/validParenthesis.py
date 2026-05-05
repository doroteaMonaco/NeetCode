class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            "}": "{",
            "]" : "[",
            ")" : "("
        }

        for ch in s:
            if ch in brackets:
                if stack and stack[-1] == brackets[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        if not stack:
            return True
        return False

#Time complexity: O(n)
#Space complexity: O(n) in the worst case when all characters are opening brackets

#Other solutions