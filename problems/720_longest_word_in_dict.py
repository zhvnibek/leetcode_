from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        all_words = set(words)
        longest = ''
        max_len = 0
        for word in sorted(words):
            prefixes = set([word[:i] for i in range(1, len(word))])
            if not prefixes.difference(all_words) and len(word) > max_len:
                max_len = len(word)
                longest = word
        return longest

if __name__ == '__main__':
    t_words = ["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"]
    print(Solution().longestWord(words=t_words))
