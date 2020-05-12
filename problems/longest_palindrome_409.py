from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        odds = False
        for letter, count in Counter(s).items():
            res += 2 * (count // 2)
            if count % 2 == 1:
                odds = True
        return res + int(odds)

if __name__ == '__main__':
    s = Solution()
    _str = "ccddsc"
    lp = s.longestPalindrome(s=_str)
    print(lp)
