

class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward_pointer = 0
        reverse_pointer = len(s) - 1

        while forward_pointer < reverse_pointer:
            while not s[forward_pointer].isalnum() and forward_pointer < reverse_pointer:
                forward_pointer += 1

            while not s[reverse_pointer].isalnum() and forward_pointer < reverse_pointer:
                reverse_pointer -= 1

            if s[forward_pointer].lower() != s[reverse_pointer].lower():
                return False

            forward_pointer += 1
            reverse_pointer -= 1

        return True


if __name__ == '__main__':
    s = Solution()

    print(s.isPalindrome("0P"))
