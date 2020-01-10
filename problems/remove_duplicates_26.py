from typing import List


class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     i, j = 0, 1
    #     while j < n:
    #         while j < n and nums[i] == nums[j]:
    #             j += 1
    #         if j < n:
    #             nums[i+1] = nums[j]
    #             i += 1
    #         j += 1
    #         print(nums)
    #     return i + 1

    # def removeDuplicates(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #     n = len(nums)
    #     i = 0
    #     for j in range(1, n):
    #         if nums[j] != nums[i]:
    #             i += 1
    #             nums[i] = nums[j]
    #     return i + 1

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 1 or n > nums[i-1]:
                nums[i] = n
                i += 1
        return i


if __name__ == '__main__':
    s = Solution()
    num_list = [0, 0, 0, 0, 1, 1, 1, 3, 3, 4, 5, 6, 6]
    ans = s.removeDuplicates(num_list)
    print(ans)
