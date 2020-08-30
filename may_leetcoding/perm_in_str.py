from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = map(len, [s1, s2])
        c1, c2 = map(Counter, [s1, s2[:l1]])
        for i in range(l1, l2):
            if c1 == c2:
                return True
            c2[s2[i-l1]] -= 1
            if c2[s2[i-l1]] == 0:
                del c2[s2[i-l1]]
            c2[s2[i]] = c2.get(s2[i], 0) + 1
        return c1 == c2


if __name__ == '__main__':
    first = "dcxa"
    second = "dcdxa"
    print(Solution().checkInclusion(s1=first, s2=second))
