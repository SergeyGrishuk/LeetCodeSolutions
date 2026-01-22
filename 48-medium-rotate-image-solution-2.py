

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        length = len(matrix)
        layer = 0

        direction = [0, 1]
        points_values = []

        while layer < length // 2: # Iterates the matrix layer by layer
            # Prepare the initial coordinates for the layer processing
            points_coordinates = [
                [0 + layer, 0 + layer],
                [0 + layer, length - 1 - layer],
                [length - 1 - layer, length - 1 - layer],
                [length - 1 - layer, 0 + layer]
            ]

            for _ in range(layer, length - 1 - layer): # Iterates each layer from index 0 up to index -2 (one before the end)
                for point in points_coordinates: # Loads the 4 current points (by coordinates) into a buffer array.
                    points_values.append(matrix[point[0]][point[1]])

                # Take the last point and insert it as the first one (i.e. rotate 90 degrees)
                last_value = points_values.pop()
                points_values.insert(0, last_value)

                # Inserts the rotated points back to the matrix
                for point in points_coordinates:
                    matrix[point[0]][point[1]] = points_values.pop(0) # Not the best idea but works for now. Might be better to use dequeue instead.

                points_values.clear() # Clear for later reuse as a buffer

                # Apply the direction on the points_coordinates
                for i in range(len(points_coordinates)):
                    points_coordinates[i] = [points_coordinates[i][0] + direction[0], points_coordinates[i][1] + direction[1]]
                    direction[0], direction[1] = direction[1], direction[0] * -1

            layer += 1


def main():
    s = Solution()

    image = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

    print(image)

    s.rotate(image)
    
    print(image)


main()
