

class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        x *= -1 if neg else 1

        rev = 0

        while x:
            rev *= 10
            rev += x % 10

            if rev.bit_length() > 31:
                rev = 0

                break

            x //= 10

        return rev * -1 if neg else rev


if __name__ == "__main__":
    s = Solution()

    print(s.reverse(-12311111111111111111111111))
