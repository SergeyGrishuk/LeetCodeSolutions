

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = []

        for i in range(rowIndex + 1):
            print(f"i = {i}")
            mid_calc_index = (i + 1) // 2
            mid_calc_index += 1 if (i + 1) % 2 != 0 else 0

            print(f"Mid Calc Index: {mid_calc_index}")

            row.append(1)

            for j in range(0, mid_calc_index):
                if j == 0:
                    continue

                row[-(j + 1)] = row[j] + row[j - 1]

            for j in range(0, mid_calc_index):
                row[j] = row[-(j + 1)]

        return row


if __name__ == '__main__':
    s = Solution()

    print(s.getRow(10))
