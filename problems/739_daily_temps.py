from typing import List


class Solution:
    def dailyTemperatures_1(self, T: List[int]) -> List[int]:
        waits = []
        for i in range(len(T)):
            for j in range(i+1, len(T)):
                if T[i] < T[j]:
                    waits.append(j-i)
                    break
            else:
                waits.append(0)
        return waits

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        waits = [0] * len(T)
        stack = []
        for i in range(len(T)-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                waits[i] = stack[-1] - i
            stack.append(i)
        return waits

if __name__ == '__main__':
    t_temp = [73, 74, 75, 71, 69, 72, 76, 73]
    res = Solution().dailyTemperatures(T=t_temp)
    print(res)
