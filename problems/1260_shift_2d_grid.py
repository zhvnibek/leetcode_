from typing import List


class Solution:
    def _shift_row(self, row: List[int], k: int = 1) -> List[int]:
        return [row[-1]] + row[:len(row)-1]

    # def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
    #     for i in range(k):
    #         grid = [self._shift_row(row) for row in grid]
    #         first_row = [row[0] for row in grid]
    #         grid[0][0] = first_row[-1]
    #         for i in range(1, len(grid)):
    #             grid[i][0] = first_row[i-1]
    #     return grid

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        for _ in range(k):
            previous = grid[-1][-1]
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    grid[row][col], previous = previous, grid[row][col]
        return grid


if __name__ == '__main__':
    s = Solution()
    g = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    print(s.shiftGrid(g, k))
    # row = [1, 2, 3]
    # print(s._shift_row(row))
