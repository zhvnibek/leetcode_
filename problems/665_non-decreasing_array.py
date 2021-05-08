"""
https://leetcode.com/problems/non-decreasing-array/discuss/1190763/JS-Python-Java-C%2B%2B-or-Simple-Solution-w-Visual-Explanation

"""

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        drop = False
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                if drop or (1 < i < n - 1 and nums[i - 2] > nums[i] and nums[i + 1] < nums[i - 1]):
                    return False
                drop = True
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.checkPossibility(nums=[4, 2, 1]))
