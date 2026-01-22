

from typing import List


# Stack: DFS
# Queue: BFS

class Solution:
    def check_if_gets_to_ocean(self, stack: list[tuple[int, int]], gets_to: set[tuple[int, int]]) -> None:
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        while stack:
            point = stack.pop()

            for direction_row, direction_col in directions:
                if 0 <= point[0] + direction_row < len(self.heights) and 0 <= point[1] + direction_col < len(self.heights[0]):
                    if self.heights[point[0] + direction_row][point[1] + direction_col] >= self.heights[point[0]][point[1]] and (point[0] + direction_row, point[1] + direction_col) not in gets_to:
                        gets_to.add((point[0] + direction_row, point[1] + direction_col))
                        stack.append((point[0] + direction_row, point[1] + direction_col))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.gets_to_pacific = set()
        self.gets_to_atlantic = set()

        self.heights = heights

        # Get all the initial points that touch each of the oceans
        for i in range(len(heights[0])):
            self.gets_to_pacific.add((0, i))
            self.gets_to_atlantic.add((len(heights) - 1, i))

        for i in range(len(heights)):
            self.gets_to_pacific.add((i, 0))
            self.gets_to_atlantic.add((i, len(heights[0]) - 1))

        pacific_stack = list(self.gets_to_pacific)
        atlantic_stack = list(self.gets_to_atlantic)

        self.check_if_gets_to_ocean(pacific_stack, self.gets_to_pacific)
        self.check_if_gets_to_ocean(atlantic_stack, self.gets_to_atlantic)

        print(self.gets_to_pacific)
        print(self.gets_to_atlantic)

        return [list(x) for x in self.gets_to_pacific.intersection(self.gets_to_atlantic)]


def main():
    s = Solution()

    print(s.pacificAtlantic([[1,1],[1,1],[1,1]]))


main()
