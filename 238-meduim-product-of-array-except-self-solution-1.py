

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1]

        right_product = 1

        for i in range(1, len(nums)):
            results.append(nums[i - 1] * results[i - 1])

        for i in range(len(nums) - 1, -1, -1):
            results[i] = results[i] * right_product
            right_product *= nums[i]

        return results


def main():
    s = Solution()

    print(s.productExceptSelf([1, 2, 3, 4]))


main()
