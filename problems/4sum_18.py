from typing import List, Set


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quads = List[List[int]] = []
        return quads

    def n_sum(self, nums):
        pass

    def two_sum(self, nums: List[int], target: int) -> List[List[int]]:
        pairs: List[List[int]] = []
        length = len(nums)
        if length < 2:
            return []
        left, right = 0, length - 1
        nums.sort()
        print(nums)
        while left < right:
            _sum = nums[left] + nums[right]
            if _sum == target:
                pairs.append([nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right-1] == nums[right]:
                    right -= 1
                left += 1
                right -= 1
            elif _sum < target:
                left += 1
            else:
                right -= 1
        return pairs


if __name__ == '__main__':
    s = Solution()
    _list = [1, 0, -1, 0, 0, 1, -2, 2]
    t = 3
    t_pairs: List[List[int]] = s.two_sum(nums=_list, target=t)
    print(t_pairs)
