

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))


if __name__ == '__main__':
    org = "the sky is blue"
    rev = Solution().reverseWords(s=org)
    print(rev)
