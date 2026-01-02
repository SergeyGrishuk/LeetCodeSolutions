

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_difference = abs(len(a) - len(b))

        if len_difference:
            a = "0" * len_difference + a if len(a) < len(b) else a
            b = "0" * len_difference + b if len(a) > len(b) else b

        result = ""

        carry = 0

        for index_a, index_b in zip(range(len(a) -1, -1, -1), range(len(b) -1, -1, -1)):
            total = int(a[index_a]) + int(b[index_b]) + carry
            result += str(total % 2)
            carry = total // 2

        if carry: result += str(carry)

        return result[::-1]


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("10", "1"))
