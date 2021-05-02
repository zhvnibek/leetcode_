from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        parts = []
        head = tail = 0
        for i, c in enumerate(S):
            tail = max(tail, last[c])
            if i == tail:
                parts.append(tail-head+1)
                head = tail + 1
        return parts

if __name__ == '__main__':
    t = "ababcbacadefegdehijhklij"
    print(Solution().partitionLabels(S=t))
