

from typing import List


# Stack: DFS
# Queue: BFS

class Solution:
    def gets_to_pacific(self, point: List[int]) -> bool:
        if point[0] == 0 or point[1] == 0:
            return True

        if self.heights[point[0] - 1][point[1]] > self.heights[point[0]][point[1]] and self.heights[point[0]][point[1] - 1] > self.heights[point[0]][point[1]]:
            return False

        # Check upwards
        got_to_water = self.gets_to_pacific([point[0] - 1, point[1]])

        if got_to_water:
            return True
        
        # Check left
        return self.gets_to_pacific([point[0], point[1] - 1])

    def gets_to_atlantic(self, point: List[int]) -> bool:
        if point[0] == len(self.heights) - 1 or point[1] == len(self.heights[0]) - 1:
            return True
        
        if self.heights[point[0] + 1][point[1]] > self.heights[point[0]][point[1]] and self.heights[point[0]][point[1] + 1] > self.heights[point[0]][point[1]]:
            return False

        # Check downwards
        got_to_water = self.gets_to_atlantic([point[0] + 1, point[1]])

        if got_to_water:
            return True
        
        # Check right
        return self.gets_to_atlantic([point[0], point[1] + 1])

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights

        coordinates = []

        for row in range(len(self.heights)):
            for col in range(len(self.heights[0])):
                if self.gets_to_pacific([row, col]) and self.gets_to_atlantic([row, col]):
                    coordinates.append([row, col])

        return coordinates


def main():
    s = Solution()

    print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))


main()
