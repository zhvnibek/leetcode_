from typing import List


class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
            print(nums)
        return i


if __name__ == '__main__':
    s = Solution()
    num_list = [0, 0, 0, 0, 1, 1, 1, 3, 3, 4, 5, 6, 6]
    ans = s.removeDuplicates(num_list)
    print(ans)
