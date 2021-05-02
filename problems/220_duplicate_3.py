from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        s = sorted(nums[:k])
        print(s)

        return False


if __name__ == '__main__':
    t_nums = [1, 3, 2, 1]
    t_k = 3
    t_t = 0
    print(Solution().containsNearbyAlmostDuplicate(nums=t_nums, k=t_k, t=t_t))
