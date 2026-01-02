

from pprint import pprint
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        nums_d = {}

        for index, number in enumerate(nums):
            if target - number in nums_d:
                return [index, nums_d[target - number]]
            else:
                nums_d[number] = index


if __name__ == '__main__':
    solution = Solution()
    print(solution.two_sum([3, 2, 4], 6))
    # print(solution.two_sum([3, 3], 6))