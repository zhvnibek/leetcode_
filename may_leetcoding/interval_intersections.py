from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        inter = []
        i = j = 0
        while i < len(A) and j < len(B):
            head = max(A[i][0], B[j][0])
            tail = min(A[i][1], B[j][1])
            if head <= tail:
                inter.append([head, tail])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return inter


if __name__ == '__main__':
    a = [[17, 20]]
    b = [[2, 3], [6, 8], [12, 14], [19, 20]]
    print(Solution().intervalIntersection(A=a, B=b))
