

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if len(nums1) == 0 or len(nums2) == 0:
            return

        sort_pointer = len(nums1) - 1
        nums1_pointer = m - 1
        nums2_pointer = n - 1

        while nums1_pointer >= 0 and nums2_pointer >= 0:
            if nums1[nums1_pointer] >= nums2[nums2_pointer]:
                nums1[sort_pointer] = nums1[nums1_pointer]
                nums1_pointer -= 1
            else:
                nums1[sort_pointer] = nums2[nums2_pointer]
                nums2_pointer -= 1

            sort_pointer -= 1

        while nums2_pointer >= 0:
            nums1[nums2_pointer] = nums2[nums2_pointer]
            nums2_pointer -= 1


if __name__ == '__main__':
    s = Solution()
    l1 = [2, 0]
    l2 = [1]
    m = 1
    n = len(l2)

    s.merge(l1, m, l2, n)
    print(l1)
