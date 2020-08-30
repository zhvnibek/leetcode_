from typing import List


class Solution:
    def get_diags(self, nums: List[List[int]]) -> int:
        max_diagonal = 1
        for row in range(len(nums)):
            max_diagonal = max(max_diagonal, len(nums[row]) + row)
        return max_diagonal

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ordered = []
        for i in range(self.get_diags(nums=nums)):
            j = 0
            while i >= 0:
                try:
                    ordered.append(nums[i][j])
                except IndexError:
                    pass
                i -= 1
                j += 1
        return ordered


if __name__ == '__main__':
    s = Solution()
    _nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    diag: List[int] = s.findDiagonalOrder(nums=_nums)
    print(diag)
