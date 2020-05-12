

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 4:
            return False
        return self.isHappy(self.sun_of_squares(n))

    def sun_of_squares(self, n: int) -> int:
        s = 0
        while n > 0:
            r = n % 10
            s += r ** 2
            n //= 10
        return s

if __name__ == '__main__':
    t = 4
    print(Solution().isHappy(n=t))


