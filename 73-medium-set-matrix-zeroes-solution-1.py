

from typing import List, Dict


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        set_to_zero: Dict[str, set] = {"rows": set(), "cols": set()}

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    set_to_zero["rows"].add(row)
                    set_to_zero["cols"].add(col)

        print(set_to_zero)

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row in set_to_zero["rows"] or col in set_to_zero["cols"]:
                    matrix[row][col] = 0


def main():
    s = Solution()

    matrix = [[1, 1, 1, 1], [1, 0, 1, 0], [1, 1, 1, 1]]

    s.setZeroes(matrix)

    print(matrix)


main()
