from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        _sum = _max = nums[0]
        for n in nums[1:]:
            _sum = n if _sum < 0 else n + _sum
            _max = max(_sum, _max)
        return _max


if __name__ == '__main__':
    t_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = Solution().maxSubArray(nums=t_nums)
    print(res)
