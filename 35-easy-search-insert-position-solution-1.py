

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            mid_pointer = (right_pointer - left_pointer) // 2 + left_pointer

            if nums[mid_pointer] == target:
                return mid_pointer

            if target > nums[mid_pointer]:
                left_pointer = mid_pointer + 1
            else:
                right_pointer = mid_pointer -1

        return left_pointer


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3], 4))
