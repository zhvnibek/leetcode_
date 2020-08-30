from typing import List


class Solution:
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def gen(self, digits: str):
        if len(digits) == 1:
            for i in self.mapping.get(digits[0], ''):
                yield i
        if len(digits) > 1:
            for i in self.mapping.get(digits[0], ''):
                for j in self.gen(digits=digits[1:]):
                    yield i+j

    def letterCombinations(self, digits: str) -> List[str]:
        return list(self.gen(digits=digits))


if __name__ == '__main__':
    t_digits = '23'
    reps = Solution().letterCombinations(digits=t_digits)
    print(reps)
