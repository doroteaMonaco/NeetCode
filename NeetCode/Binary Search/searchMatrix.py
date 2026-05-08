

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        i = 0
        j = (ROWS * COLS) -1  

        while i <= j:
            m = (i + j) // 2
            r = m // COLS
            c = m % COLS
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                j = m - 1 
            else:
                i = m + 1

        return False
            
# Time complexity: O(log(m*n)) where m is the number of rows and n is the number of columns in the input matrix. This is because we are halving the search space in each iteration of the while loop.
# Space complexity: O(1) because we are using only a constant amount of extra space 

# Other solutions
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1

        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False
        
# Time complexity: O(m + n) where m is the number of rows and n is the number of columns in the input matrix. This is because in the worst case, we might have to traverse all the way from the top-right corner to the bottom-left corner of the matrix.
# Space complexity: O(1) because we are using only a constant amount of extra space