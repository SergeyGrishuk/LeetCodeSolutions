

class Solution:
    def myAtoi(self, s: str) -> int:
        pointer = 0
        neg = False

        max_value = (2 ** 31) - 1
        min_value = -2 ** 31

        result = 0

        # Stage I, skip leading spaces.
        while pointer < len(s) and s[pointer] == " ":
            pointer += 1

        # Stage II, get signature
        if pointer < len(s) and (s[pointer] == "+" or s[pointer] == "-"):
            if s[pointer] == "-":
                neg = True

            pointer += 1

        # Stage III, parse numbers
        while pointer < len(s) and s[pointer].isdigit():
            digit = int(s[pointer])

            if result > max_value // 10 or (result == max_value // 10 and digit > 7):
                if neg:
                    return min_value
                else:
                    return max_value
            
            result *= 10
            result += digit

            pointer += 1

        return result if not neg else result * -1


def main():
    s = Solution()

    print(s.myAtoi("-123111111121"))


main()
