from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1):
                return False
        return True


if __name__ == '__main__':
    coords = [[-7, -3], [-7, -1], [-2, -2], [0, -8], [2, -2], [5, -6], [5, -5], [1, 7]]
    print(Solution().checkStraightLine(coordinates=coords))
