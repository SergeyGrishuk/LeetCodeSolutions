

from typing import List


class Solution:
    def apply_direction(self, pointer: List[int], direction: List[int]) -> None:
        for i in range(len(pointer)):
            pointer[i] += direction[i]


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        total_rows = len(matrix)
        total_cols = len(matrix[0])
        
        pointer = [0, 0] # row, col
        direction = [0, 1]

        bounds_rows = [0, total_rows - 1]
        bounds_cols = [0, total_cols - 1]

        result = []

        while len(result) < total_rows * total_cols:
            result.append(matrix[pointer[0]][pointer[1]])

            if direction[0]:
                if not bounds_rows[0] <= pointer[0] + direction[0] <= bounds_rows[1]:
                    direction[0], direction[1] = direction[1], direction[0] * -1
                    
                    if direction[1] == 1:
                        bounds_cols[0] += 1
                    elif direction[1] == -1:
                        bounds_cols[1] -= 1
            else:
                if not bounds_cols[0] <= pointer[1] + direction[1] <= bounds_cols[1]:
                    direction[0], direction[1] = direction[1], direction[0] * -1

                    if direction[0] == 1:
                        bounds_rows[0] += 1
                    elif direction[0] == -1:
                        bounds_rows[1] -= 1

            self.apply_direction(pointer, direction)

        return result


def main():
    s = Solution()

    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))


main()
