from typing import List


class Solution:

    def are_ordered(self, first: str, second: str, order: str):
        """Return True iff the first word is less than or equal to the second word lexicographically"""
        print(f'Comparing {first} and {second}')
        n, m = len(first), len(second)
        for i in range(min(n, m)):
            o, p = order.index(first[i]), order.index(second[i])
            if o < p:
                return True
            elif o > p:
                return False
        return n <= m

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            if not self.are_ordered(first=words[i], second=words[i+1], order=order):
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    t_words = ["hello", "leetcode", 'h']
    t_order = "hlabcdefgijkmnopqrstuvwxyz"
    print(s.isAlienSorted(words=t_words, order=t_order))

