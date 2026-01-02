

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for number in nums:
            result ^= number

        return result


if __name__ == '__main__':
    s = Solution()

    print(s.singleNumber([1, 2, 1, 2, 3]))
