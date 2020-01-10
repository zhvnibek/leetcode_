from typing import List


class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        n = len(x)
        if n < 4:
            return False
        for i in range(3, n):
            if x[i - 3] >= x[i - 1] and x[i] >= x[i - 2]:
                return True
            elif i == 4 and x[i - 1] == x[i - 3] and x[i - 4] + x[i] >= x[i - 2]:
                return True
            elif i >= 5 and x[i - 4] <= x[i - 2] <= x[i] + x[i - 4] and x[i - 1] + x[i - 5] >= x[i - 3] >= x[i - 1]:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    test = [1,2,3,4]
    print(s.isSelfCrossing(test))
