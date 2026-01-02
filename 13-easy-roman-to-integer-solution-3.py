from unittest import skip


class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}

        result = 0

        for i in range(len(s) - 1):
            if numerals[s[i]] >= numerals[s[i + 1]]:
                result += numerals[s[i]]
            else:
                result -= numerals[s[i]]

        result += numerals[s[-1]]

        return result


if __name__ == '__main__':
    s = Solution()

    print(s.romanToInt("IX"))