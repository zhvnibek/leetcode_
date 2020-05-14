

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            while k > 0 and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        if k > 0:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'


if __name__ == '__main__':
    t_num = "1432219"
    t_k = 3
    print(Solution().removeKdigits(num=t_num, k=t_k))