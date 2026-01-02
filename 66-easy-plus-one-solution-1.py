

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        add_one = True

        increased_reversed_number = []

        for digit in reversed(digits):
            if add_one:
                digit += 1
                add_one = False

            if digit > 9:
                digit = 0
                add_one = True

            increased_reversed_number.append(digit)

        if add_one:
            increased_reversed_number.append(1)

        return increased_reversed_number[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1, 9]))
