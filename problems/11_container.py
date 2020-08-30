from typing import List


class Solution:
    def brute_maxArea(self, height: List[int]) -> int:
        n = len(height)
        _max_area = 0
        for i in range(n):
            for j in range(i+1, n):
                _max_area = max((j-i)*min(height[i], height[j]), _max_area)
        return _max_area

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        _max_area = 0
        while left < right:
            _max_area = max(min(height[left], height[right]) * (right - left), _max_area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return _max_area


if __name__ == '__main__':
    s = Solution()
    h = [1, 1]
    # h = [1, 2, 3, 4, 1, 7, 4, 8, 1, 5]
    # max_area = s.brute_maxArea(height=h)
    max_area = s.maxArea(height=h)
    print(max_area)
