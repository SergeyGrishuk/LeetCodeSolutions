

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        side_length = len(matrix)

        for row in range(len(matrix) // 2):
            for col in range(row, len(matrix[row]) - 1 - row):
                matrix[row][col], matrix[col][side_length-1-row], matrix[side_length-1-row][side_length-1-col], matrix[side_length-1-col][row] = \
                matrix[side_length-1-col][row], matrix[row][col], matrix[col][side_length-1-row], matrix[side_length-1-row][side_length-1-col]


def main():
    s = Solution()

    image = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

    print(image)

    s.rotate(image)
    
    print(image)


main()
