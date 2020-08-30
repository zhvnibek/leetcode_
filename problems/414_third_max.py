from typing import List


class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        _set: set = set(nums[:3])
        print(_set)
        for n in nums[3:]:
            _set.add(n)
            _set = set(sorted(_set, reverse=True)[:3])
            print(_set)
        return min(_set) if len(_set) == 3 else max(_set)


if __name__ == '__main__':
    s = Solution()
    _list = [3, 3, 5, 3, 6, 0, 1]
    tm = s.thirdMax(nums=_list)
    print(tm)
