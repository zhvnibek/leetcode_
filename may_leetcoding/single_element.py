from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        head, tail = 0, len(nums) - 1
        mid = (tail + head) // 2
        if (mid - head) % 2 == 0:
            if nums[mid] == nums[mid - 1]:
                return self.singleNonDuplicate(nums[head: mid-1])
            elif nums[mid] == nums[mid + 1]:
                return self.singleNonDuplicate(nums[mid+2: tail+1])
            return nums[mid]
        else:
            if nums[mid] == nums[mid-1]:
                return self.singleNonDuplicate(nums[mid+1: tail+1])
            elif nums[mid] == nums[mid+1]:
                return self.singleNonDuplicate(nums[head: mid])
            return nums[mid]


if __name__ == '__main__':
    # t_nums = [3]
    # t_nums = [1, 1, 2]
    t_nums = [3, 5, 5, 6, 6]
    print(Solution().singleNonDuplicate(nums=t_nums))
