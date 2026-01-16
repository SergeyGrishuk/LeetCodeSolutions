

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

        for numeral, value in numerals.items():
            while num >= value:
                final += numeral
                num -= value

        return final


def main():
    s = Solution()

    print(s.intToRoman(3749))


main()
