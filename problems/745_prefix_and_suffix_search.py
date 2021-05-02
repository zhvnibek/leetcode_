from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self._word_var2indices = {}
        for i, word in enumerate(words):
            word_len = len(word)
            for suffix_start in range(word_len, -1, -1):
                for prefix_end in range(word_len+1):
                    self._word_var2indices[f'{word[suffix_start:]}#{word[:prefix_end]}'] = i

    def f(self, prefix: str, suffix: str) -> int:
        return self._word_var2indices.get(f"{suffix}#{prefix}", -1)


if __name__ == "__main__":
    t_words = ['test', 'tesdt']
    t_prefix = 'te'
    t_suffix = 't'
    wf = WordFilter(words=t_words)
    found = wf.f(prefix=t_prefix, suffix=t_suffix)
    print(found)
