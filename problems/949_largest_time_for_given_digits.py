from typing import List
from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, A: List[int]):
        out = ""
        for P in permutations(A):
            if P[0] * 10 + P[1] <= 23 and P[2] <= 5:
                out = max(out, f'{P[0]}{P[1]}:{P[2]}{P[3]}')
        return out


class Solution2:
    def time_permutations(self, digits):
        for h1, h2, m1, m2 in permutations(digits):
            if h1 * 10 + h2 < 24 and m1 < 6:
                yield f"{h1}{h2}:{m1}{m2}"

    def largestTimeFromDigits(self, A: List[int]):
        return max(self.time_permutations(A), default="")

if __name__ == '__main__':
    t_a = [3, 1, 1, 2]
    print(Solution2().largestTimeFromDigits(A=t_a))
