class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        mod = 1000000007
        is_prime = [1 for i in range(n + 1)]
        p = 2
        while p * p <= n:
            if is_prime[p] == 1:
                for i in range(p * 2, n + 1, p):
                    is_prime[i] = 0
            p += 1
        is_prime[0] = 0
        is_prime[1] = 0
        n_primes = sum(is_prime)
        ans = 1
        for i in range(2, n_primes + 1):
            ans = (ans * i) % mod
        for i in range(2, n - n_primes + 1):
            ans = (ans * i) % mod
        return ans


if __name__ == '__main__':
    s = Solution()
    k = 100
    print(s.numPrimeArrangements(k))
