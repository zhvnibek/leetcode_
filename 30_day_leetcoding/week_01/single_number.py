"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = nums[0]
        for n in nums[1:]:
            k ^= n
        return k

if __name__ == '__main__':
    t_nums = [4, 1, 2, 1, 2]
    res = Solution().singleNumber(nums=t_nums)
    print(4 ^ 1 ^ 2 ^ 1 ^ 2)
