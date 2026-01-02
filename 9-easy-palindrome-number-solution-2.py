

class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_number = 0
        original_number = x

        while x > 0:
            print(f"x: {x}")
            print(f"reversed number: {reversed_number}")

            last_digit = x % 10

            x = x // 10
            reversed_number *= 10
            reversed_number += last_digit

        print(f"original number: {original_number}, reversed_number: {reversed_number}")
        return original_number == reversed_number


if __name__ == '__main__':
    s = Solution()
    print(s.is_palindrome(1000001))

    # print(s.get_last_digit(5))
