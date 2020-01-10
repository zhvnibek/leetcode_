from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # f(i) = cost(i) + min(f(i-1), f(i-2))
        if len(cost) == 2:
            min(cost)
        opt_costs: list = cost[:2]
        for i in range(2, len(cost)):
            opt_costs.append(cost[i] + min(opt_costs[i-1], opt_costs[i-2]))
            print(opt_costs)
        return min(opt_costs[-1], opt_costs[-2])


if __name__ == '__main__':
    s = Solution()
    test = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(s.minCostClimbingStairs(test))
