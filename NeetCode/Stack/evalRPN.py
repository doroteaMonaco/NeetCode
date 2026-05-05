class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for ch in tokens:
            if ch == "+":
                b = stack.pop()
                a = stack.pop()
                res = (a + b)
                stack.append(res)
            elif ch == "-":
                b = stack.pop()
                a = stack.pop()
                res = (a - b)
                stack.append(res)
            elif ch == "*":
                b = stack.pop()
                a = stack.pop()
                res = (a * b)
                stack.append(res)
            elif ch == "/":
                b = stack.pop()
                a = stack.pop()
                res = (int(a / b))
                stack.append(res)
            else:
                stack.append(int(ch))
        
        return stack[0]

#Time complexity: O(n) where n is the number of tokens
#Space complexity: O(n) in the worst case when all tokens are numbers and no operators are present, resulting in all tokens being pushed onto the stack.

#Others Solutions
#Double Linked List to implement the stack, where each node contains a value and a pointer to the next node. This allows for efficient push and pop operations while maintaining the order of the tokens.

from typing import List
class DoublyLinkedList:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        head = DoublyLinkedList(tokens[0])
        curr = head

        for i in range(1, len(tokens)):
            curr.next = DoublyLinkedList(tokens[i], prev=curr)
            curr = curr.next

        while head is not None:
            if head.val in "+-*/":
                l = int(head.prev.prev.val)
                r = int(head.prev.val)
                if head.val == '+':
                    res = l + r
                elif head.val == '-':
                    res = l - r
                elif head.val == '*':
                    res = l * r
                else:
                    res = int(l / r)

                head.val = str(res)
                head.prev = head.prev.prev.prev
                if head.prev is not None:
                    head.prev.next = head

            ans = int(head.val)
            head = head.next

        return ans
    
#Time complexity: O(n) where n is the number of tokens
#Space complexity: O(n) in the worst case when all tokens are numbers and no operators

#Recursive approach, where we recursively evaluate the expression by processing the tokens from the end to the beginning, using a helper function to perform the operations.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)

            right = dfs()
            left = dfs()

            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)

        return dfs()
    
#Time complexity: O(n) where n is the number of tokens
#Space complexity: O(n) in the worst case when all tokens are numbers and no operators are present, resulting in a recursion depth of n.