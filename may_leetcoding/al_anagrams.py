from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cp = Counter(p)
        # return [i for i in range(len(s)-len(p)+1) if Counter(s[i:i+len(p)]) == cp]
        ls, lp = len(s), len(p)
        cc = Counter(s[:lp])
        ids = [0] if cc == cp else []
        for i in range(1, ls-lp+1):
            cc[s[i-1]] -= 1
            if cc[s[i-1]] == 0:
                del cc[s[i-1]]
            cc[s[i+lp-1]] = cc.get(s[i+lp-1], 0) + 1
            if cc == cp:
                ids.append(i)
        return ids

if __name__ == '__main__':
    ts = "cbaebabacd"
    tp = "abc"
    print(Solution().findAnagrams(s=ts, p=tp))
