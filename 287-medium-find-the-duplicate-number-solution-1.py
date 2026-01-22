

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


def main():
    s = Solution()

    print(s.findDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]))


main()
