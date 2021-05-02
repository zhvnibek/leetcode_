from typing import List


class Solution:
    ans = None

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.helper(nums, [])
        return self.ans

    def helper(self, nums, temp):
        if len(nums) == 0:
            self.ans.append(temp)
            return

        for i in range(len(nums)):
            self.helper(nums=nums[:i] + nums[i + 1:], temp=temp + [nums[i]])


if __name__ == '__main__':
    print(Solution().permute(nums=[1, 2, 3]))
