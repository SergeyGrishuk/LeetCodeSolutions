

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        iterations = 0

        while left <= right:
            iterations += 1
            print(f"Interation: {iterations}")
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1

        return right


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(0))
