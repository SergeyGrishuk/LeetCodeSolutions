

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        _map = []

        down = True
        index_to_write = {"x": 0, "y": 0}


        for _ in range(numRows):
            _map.append([None] * len(s))

        for char in s:
            _map[index_to_write["y"]][index_to_write["x"]] = char

            if index_to_write["y"] == numRows - 1:
                down = False
            elif index_to_write["y"] == 0:
                down = True

            if down:
                index_to_write["y"] += 1
            else:
                index_to_write["y"] -= 1 if index_to_write["y"] > 0 else 0
                index_to_write["x"] += 1

        final_str = ""

        for line in _map:
            final_str += "".join([x for x in line if x])

        return final_str


if __name__ == "__main__":
    s = Solution()

    print(s.convert("PAYPALISHIRING", 4))
