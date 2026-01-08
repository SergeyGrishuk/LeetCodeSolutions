

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        strs = [""] * numRows

        direction = 1
        current_row = 0

        for char in s:
            strs[current_row] += char

            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        return "".join(strs)


if __name__ == "__main__":
    s = Solution()

    print(s.convert("PAYPALISHIRING", 1))
