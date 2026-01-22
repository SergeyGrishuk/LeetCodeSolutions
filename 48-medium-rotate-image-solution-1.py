

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Flip the matrix upside down
        for i in range(len(matrix) // 2):
            matrix[i], matrix[-(i + 1)] = matrix[-(i + 1)], matrix[i]

        # Transpose all the elements (replace diagonally)
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def main():
    s = Solution()

    image = [[1,2,3],[4,5,6],[7,8,9]]

    print(image)

    s.rotate(image)
    
    print(image)


main()
