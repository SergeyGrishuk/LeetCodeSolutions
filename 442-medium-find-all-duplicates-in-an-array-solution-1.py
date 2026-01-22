

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []

        for i in range(len(nums)):
            val = abs(nums[i])
            target_index = val - 1

            if nums[target_index] < 0:
                duplicates.append(val)
            else:
                nums[target_index] *= - 1

        return duplicates


def main():
    s = Solution()

    print(s.findDuplicates([1, 2, 2, 3, 4, 5, 6, 7, 7, 8]))


main()
