from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        return [sum([int(q_r ** 2 >= (q_x - p_x) ** 2 + (q_y - p_y) ** 2) for p_x, p_y in points]) for q_x, q_y, q_r in queries]


if __name__ == '__main__':
    s = Solution()
    points = [[1, 3], [3, 3], [5, 3], [2, 2]]
    queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
    answer = s.countPoints(points, queries)
    print(answer)
