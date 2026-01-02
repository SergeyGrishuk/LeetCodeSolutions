from http.cookiejar import cut_port_re
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writer = 0

        for current_value in nums:
            if current_value != val:
                nums[writer] = current_value
                writer += 1

        return writer


if __name__ == '__main__':
    s = Solution()

    numbers = [0,1,2,2,3,0,4,2]
    print(s.removeElement(numbers, 2))
    print(numbers)
