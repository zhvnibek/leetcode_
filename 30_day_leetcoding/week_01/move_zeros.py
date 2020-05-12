from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        p, q = 0, 1
        for q in range(n):
            if nums[p] != 0:
                p += 1
            elif nums[q] != 0:
                nums[p], nums[q] = nums[q], 0
                p += 1
        print(nums)


if __name__ == '__main__':
    t_nums = [2, 0, 0, 1, 0, 1]
    Solution().moveZeroes(nums=t_nums)
