

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # range(start, stop, step)
        for index in range(len(digits) -1, -1, -1):
            if digits[index] == 9:
                digits[index] = 0

                continue
            digits[index] += 1

            return digits

        return [1] + digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 9]))
