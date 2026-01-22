

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_f_row = False
        zero_f_col = False

        # Stage I: Check the first row and column
        for val in matrix[0]:
            if val == 0:
                zero_f_row = True

                break

        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                zero_f_col = True

                break

        # Instead of the loops above, the `any()` function can be used.
        # zero_f_row = any(val == 0 for val in matrix[0])
        # zero_f_col = any(row[0] == 0 for row in matrix)
        #
        # It will not affect the overall complexity

        # Stage II: Check the "inner" matrix and set "flags" accordingly.
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        # Stage III: Replace the values in the matrix
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[row])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # Stage IV: Handle the updates for the first row and column.
        if zero_f_row:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0

        if zero_f_col:
            for row in range(len(matrix)):
                matrix[row][0] = 0
                

def main():
    s = Solution()

    matrix = [[1, 1, 1, 1], [1, 0, 1, 0], [1, 1, 1, 1]]

    s.setZeroes(matrix)

    print(matrix)


main()
