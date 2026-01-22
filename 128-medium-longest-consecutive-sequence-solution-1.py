

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest_sequence = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                i = 0

                while num + i in nums_set:
                    i += 1

                if i > longest_sequence:
                    longest_sequence = i

        return longest_sequence


def main():
    s = Solution()

    # print(s.longestConsecutive([100,4,200,1,3,2]))
    print(s.longestConsecutive([1, 2, 3, 4]))


main()
