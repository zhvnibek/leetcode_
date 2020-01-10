class Solution:
    def rotate(self, nums, k) -> None:
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    @staticmethod
    def reverse(nums, start, end) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    s = Solution()
    nums_test: list = [0, 1, 2, 3, 4, 5, 6]
    k_test: int = 3
    s.rotate(nums=nums_test, k=k_test)
    print(nums_test)
