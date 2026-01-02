

class Solution:
    def is_palindrome(self, x: int) -> bool:
        print(f"Checking: {x}")

        x_str = str(x)

        for i in range(len(x_str) // 2):
            if not x_str[i] == x_str[(i + 1) * -1]:
                return False

        return True


    def get_divider(self, x: int, divider: int = 1) -> int:
        if x // divider == 1:
            return divider
        else:
            return self.get_divider(x, divider * 10)

if __name__ == '__main__':
    s = Solution()
    print(s.is_palindrome(12))

    # print(s.get_divider(1234))
