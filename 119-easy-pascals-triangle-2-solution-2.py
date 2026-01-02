

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []

        for i in range(rowIndex + 1):
            row.append(1)

            for j in range(-2, -(i + 1), -1):
                row[j] = row[j] + row[j - 1]

        return row


if __name__ == '__main__':
    s = Solution()

    print(s.getRow(4))
