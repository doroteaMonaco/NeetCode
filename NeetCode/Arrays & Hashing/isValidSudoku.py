from typing import List


class Solution:
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        if (len(board) != 9) and (len(board[0]) != 9):
            return False
        
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j].isdigit() and int(board[i][j]) in seen:
                    return False
                elif board[i][j].isdigit() == False:
                    continue
                else:
                    seen.add(int(board[i][j]))
        
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j].isdigit() and int(board[i][j]) in seen:
                    return False
                elif board[i][j].isdigit() == False:
                    continue
                else:
                    seen.add(int(board[i][j]))

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j

                    if board[row][col].isdigit() and int(board[row][col]) in seen:
                        return False
                    elif board[row][col].isdigit() == False:
                        continue
                    else:
                        seen.add(int(board[row][col]))

        return True

#This is not the optimal solution.
#Time complexity: O(n^2) because we iterate through the board three times, once for the rows, once for the columns, and once for the 3x3 squares. The space complexity is O(n) because we use a set to keep track of the seen numbers in each row, column, and square.

#Other solutions
#Hash Set: we can use a hash set to keep track of the seen numbers in each
#for each cell we can check if the number is already in the hash set for the corresponding row, column, and square. If it is, we return False, otherwise we add it to the hash set. The time complexity of this solution is O(n^2) because we iterate through the board once, and the space complexity is O(n) because we use a hash set to keep track of the seen numbers.
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
    
#Time complexity: O(n^2) because we iterate through the board once, and the space complexity is O(n) because we use hash sets to keep track of the seen numbers in each row, column, and square.

#Bitmask
#Every digit can be represented using a single bit in an integer. for example, 1 uses bit 0, 
#2 uses bit 1, and so on. We can use three arrays of integers to keep track of the seen numbers in each row, column, and square. For each cell, we can check if the corresponding bit is already set in the integer for the corresponding row, column, and square. If it is, we return False, otherwise we set the bit in the integer. The time complexity of this solution is O(n^2) because we iterate through the board once, and the space complexity is O(1) because we use a fixed number of integers to keep track of the seen numbers.

#This means we can track which digits have appeared in a row, column or 3x3 square using just one inetegrer per row/column/box instead of an hash set.
#When we encounter a dgit, we compute its bit position and check if that bit is already set in teh row, duplicate in row; same fro column and box.

#convert teh digit to a bit index by subtracting 1 from the digit (since digits are 1-9 and bit indices are 0-8), and then we can check if the bit at that index is already set in the corresponding row, column, or box integer. If it is, we return False, otherwise we set that bit in the corresponding integer.
#compute the mask for the current digit by shifting 1 to the left by the bit index, and then we can check if that bit is already set in the corresponding row, column, or box integer using a bitwise AND operation. If it is, we return False, otherwise we set that bit in the corresponding integer using a bitwise OR operation.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                val = int(board[r][c]) - 1
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
                    return False

                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[(r // 3) * 3 + (c // 3)] |= (1 << val)

        return True