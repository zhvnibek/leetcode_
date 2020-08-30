from typing import List

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        triplets = []
        for i in range(size-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            head, tail = i + 1, size - 1
            while head < tail:
                three_sum = nums[i] + nums[head] + nums[tail]
                if three_sum == 0:
                    triplets.append([nums[i], nums[head], nums[tail]])
                    while head < tail and nums[head] == nums[head+1]:
                        head += 1
                    while head < tail and nums[tail] == nums[tail - 1]:
                        tail -= 1
                    head += 1
                    tail -= 1
                elif three_sum < 0:
                    head += 1
                else:
                    tail -= 1
        return triplets


if __name__ == '__main__':
    t_nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums=t_nums))
