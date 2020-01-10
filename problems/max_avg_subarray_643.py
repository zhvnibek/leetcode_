from typing import List


class Solution:
    # def findMaxAverage(self, nums: List[int], k: int) -> float:
    #     run_sum: list = [0] + nums[:1]
    #     for i in range(1, len(nums)):
    #         run_sum.append(nums[i] + run_sum[-1])
    #     n = len(nums)
    #     return max([(run_sum[i+k] - run_sum[i]) / k for i in range(n-k+1)])

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pre_sum = sum(nums[:k])
        max_sum = pre_sum
        for i in range(k, len(nums)):
            pre_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, pre_sum)
        return max_sum / k


if __name__ == '__main__':
    s = Solution()
    test = [1, 12, -5, -6, 50, 3]
    # test = [5]
    # test = [0,1,1,3,3]
    k = 4
    print(s.findMaxAverage(test, k))
