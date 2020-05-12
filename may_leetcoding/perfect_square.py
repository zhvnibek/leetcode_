class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i * i <= num:
            if num % i == 0 and num / i == i:
                return True
            i = i + 1
        return False


if __name__ == '__main__':
    t_num = 25
    print(Solution().isPerfectSquare(num=t_num))
