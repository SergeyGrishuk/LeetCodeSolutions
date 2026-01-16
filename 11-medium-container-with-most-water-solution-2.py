

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left

            max_area = h * w if h * w > max_area else max_area

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area


def main():
    s = Solution()

    print(s.maxArea([1,8,6,2,5,4,8,3,7]))

main()
