

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list_a = nums1 if len(nums1) < len(nums2) else nums2
        list_b = nums2 if list_a is nums1 else nums1

        left = 0
        right = len(list_a)

        while True:
            cut_a = (left + right) // 2
            cut_b = (len(list_a) + len(list_b) + 1) // 2 - cut_a

            if cut_a - 1 < 0:
                a_left = float("-inf")
            else:
                a_left = list_a[cut_a - 1]

            if cut_a >= len(list_a):
                a_right = float("inf")
            else:
                a_right = list_a[cut_a]

            if cut_b - 1 < 0:
                b_left = float("-inf")
            else:
                b_left = list_b[cut_b - 1]

            if cut_b >= len(list_b):
                b_right = float("inf")
            else:
                b_right = list_b[cut_b]

            if a_left > b_right:
                right = cut_a - 1
                continue

            if b_left > a_right:
                left = cut_a + 1
                continue

            if (len(list_a) + len(list_b)) % 2 == 0:
                return (max(a_left, b_left) + min(a_right, b_right)) / 2

            return max(a_left, b_left)


def main():
    s = Solution()

    print(s.findMedianSortedArrays([1, 2], [-1, 3]))


main()

