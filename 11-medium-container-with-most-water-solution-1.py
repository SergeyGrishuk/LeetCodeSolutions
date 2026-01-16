

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        for i in range(len(height)):
            for j in range(i, len(height)):
                h = min(height[i], height[j])
                w = j - i

                max_area = h * w if h * w > max_area else max_area

        return max_area


def main():
    s = Solution()

    print(s.maxArea([1,8,6,2,5,4,8,3,7]))

main()
