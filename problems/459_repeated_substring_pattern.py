

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        for i in range(1, size//2+1):
            if size % i == 0 and s[:i] * (size//i) == s:
                return True
        return False

        # Second solution:
        # If s has repeated substring pattern, then we can find s in s_fold. Otherwise, s cannot be found.
        # s_fold = s[1:] + s[:-1]
        # return s in s_fold

if __name__ == '__main__':
    t = 'ab'
    print(Solution().repeatedSubstringPattern(s=t))
