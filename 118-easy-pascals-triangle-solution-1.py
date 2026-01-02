

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            triangle.append([])

            for cell in range(row + 1):
                if cell == 0 or cell == row:
                    triangle[row].append(1)

                    continue

                triangle[row].append(triangle[row - 1][cell] + triangle[row - 1][cell - 1])

        return triangle



if __name__ == '__main__':
    s = Solution()

    print(s.generate(10))