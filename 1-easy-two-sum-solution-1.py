

from pprint import pprint
from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        nums_d = {}

        for index, number in enumerate(nums):
            if nums_d.get(number, None):
                nums_d[number].append(index)
            else:
                nums_d[number] = [index]

        # pprint(nums_d)
        i = 0

        for k, v in nums_d.items():
            pprint(f"k: {k}")

            if nums_d.get(target - k, None):
                if k == target - k:
                    if nums_d[k][0] == nums_d[target - k][0] and len(nums_d[k]) > 1:
                        i += 1
                    else:
                        continue

                return [nums_d[k][0], nums_d[target - k][0 + i]]


if __name__ == '__main__':
    solution = Solution()
    print(solution.two_sum([3, 2, 4], 6))
    # print(solution.two_sum([3, 3], 6))