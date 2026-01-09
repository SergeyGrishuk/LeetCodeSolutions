

class Solution:
    def reverse(self, x: int) -> int:
        limit = 214748364

        neg = x < 0
        x *= -1 if neg else 1 # Or use abs(x)

        rev = 0

        while x:
            if rev > limit: # Check if it is save to multiply rev by 10
                rev = 0

                break

            if rev == limit and x % 10 > 7:
                rev = 0

                break

            rev *= 10
            rev += x % 10

            x //= 10

        return rev * -1 if neg else rev


if __name__ == "__main__":
    s = Solution()

    print(s.reverse(-1231111111))
