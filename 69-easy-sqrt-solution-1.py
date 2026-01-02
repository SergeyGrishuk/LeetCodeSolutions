

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while True:
            mid = (left + right + 1) // 2

            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                right = mid
            else:
                left = mid


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(16))
