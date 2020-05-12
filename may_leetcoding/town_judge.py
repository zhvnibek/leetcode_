from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0] * N
        for i, j in trust:
            count[i-1] -= 1
            count[j-1] += 1
        for i in range(N):
            if count[i] == N - 1:
                return i+1
        return -1

if __name__ == '__main__':
    t_n = 3
    t_trust = [[1, 3], [2, 3]]
    print(Solution().findJudge(N=t_n, trust=t_trust))

