from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        desc = sorted(A, reverse=True)
        for i in range(len(desc) - 2):
            a, b, c = desc[i:i+3]
            if 2 * a < a + b + c:
                return a + b + c
        return 0

if __name__ == '__main__':
    s = Solution()
    lenghts = [2, 1, 1]
    lp = s.largestPerimeter(A=lenghts)
    print(lp)
