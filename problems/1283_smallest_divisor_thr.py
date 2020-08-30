import math
from typing import List


class Solution:
    def sum_quotients(self, nums: List[int], divisor: int) -> int:
        return sum([math.ceil(num/divisor) for num in nums])


    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        sq = threshold + 1
        d_min = 100
        d = 0
        while sq > threshold:
            d += 1
            sq = self.sum_quotients(nums, d)
            d_min = min(d, d_min)
        return d


if __name__ == '__main__':
    s = Solution()
    ns = [1, 2, 5, 9]
    t = 6
    res = s.smallestDivisor(nums=ns, threshold=t)
    print(res)
    # sq = s.sum_quotients(ns, 5)
    # print(sq)