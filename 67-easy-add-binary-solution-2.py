

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""

        carry = 0

        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0:
            a_value = int(a[i]) if i >= 0 else 0
            b_value = int(b[j]) if j >= 0 else 0

            total = a_value + b_value + carry
            result += str(total % 2)
            carry = total // 2

            i -= 1
            j -= 1

        if carry: result += str(carry)

        return result[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("10", "111"))
