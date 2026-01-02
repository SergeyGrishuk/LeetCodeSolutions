

class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward_pointer = 0
        reverse_pointer = len(s) - 1

        abc_set = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

        while forward_pointer < reverse_pointer:
            while s[forward_pointer].lower() not in abc_set and forward_pointer < len(s) - 1:
                forward_pointer += 1

            while s[reverse_pointer].lower() not in abc_set and reverse_pointer > 0:
                reverse_pointer -= 1

            tested_char_1 = s[forward_pointer].lower() if s[forward_pointer].lower() in abc_set else " "
            tested_char_2 = s[reverse_pointer].lower() if s[reverse_pointer].lower() in abc_set else " "

            if tested_char_1 != tested_char_2:
                return False

            forward_pointer += 1
            reverse_pointer -= 1

        return True


if __name__ == '__main__':
    s = Solution()

    print(s.isPalindrome("0P"))
