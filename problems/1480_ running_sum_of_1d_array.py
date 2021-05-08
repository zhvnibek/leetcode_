from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        r_sum = 0
        for i in range(len(nums)):
            r_sum += nums[i]
            nums[i] = r_sum
        return nums


if __name__ == "__main__":
    t_nums = [1, 2, 3, 4]
    s = Solution()
    print(s.runningSum(nums=t_nums))
