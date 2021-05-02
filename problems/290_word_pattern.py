

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(words) != len(pattern):
            return False

        word2pat = {}
        pat2word = {}
        for word, pat in zip(words, pattern):
            if word not in word2pat:
                if pat in pat2word:
                    return False
                word2pat[word] = pat
                pat2word[pat] = word
            elif word2pat[word] != pat:
                return False
        return True

if __name__ == '__main__':
    t_pattern = 'abba'
    t_str = 'dog dog dog dog'
    print(Solution().wordPattern(pattern=t_pattern, str=t_str))
