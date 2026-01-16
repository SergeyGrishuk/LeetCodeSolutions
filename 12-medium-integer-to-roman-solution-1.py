

class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
            }

        final = ""

        while num > 0:
            for numeral in numerals.keys():
                if num - numerals[numeral] >= 0:
                    final += numeral

                    num -= numerals[numeral]

                    break

        return final


def main():
    s = Solution()

    print(s.intToRoman(3749))


main()
