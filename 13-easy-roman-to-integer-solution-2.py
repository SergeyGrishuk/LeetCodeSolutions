from unittest import skip


class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}

        result = 0

        for index, numeral in enumerate(s):
            is_last = len(s) == index + 1

            print(f"Checking numeral: {numeral}. is_last: {is_last}")

            if not is_last:
                if numerals[s[index]] >= numerals[s[index + 1]]:
                    result += numerals[numeral]
                else:
                    result += numerals[s[index]] * -1
            else:
                result += numerals[numeral]

        return result


if __name__ == '__main__':
    s = Solution()

    print(s.romanToInt("IX"))