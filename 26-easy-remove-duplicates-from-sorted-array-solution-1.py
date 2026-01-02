

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer = 0

        # In this case, using the name `value` is more accurate then `i`
        # as `i` stands for index.
        for value in nums:
            if value > nums[writer]:
                writer += 1
                nums[writer] = value

        return writer + 1


if __name__ == '__main__':
    s = Solution()

    numbers = [0,0,1,1,1,2,2,3,3,4]

    print(s.removeDuplicates(numbers))
    print(numbers)
