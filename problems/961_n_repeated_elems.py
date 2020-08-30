from typing import List
from collections import Counter


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        counter = Counter(A)
        return counter.most_common(1)[0][0]


if __name__ == '__main__':
    s = Solution()
    k = [1,1,2,3]
    print(s.repeatedNTimes(k))
