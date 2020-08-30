
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):
        weight = 1
        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]
        self.stack.append((price, weight))
        return weight

if __name__ == '__main__':
    ss = StockSpanner()
    ss.next(price=100)
    ss.next(price=80)
    ss.next(price=60)
    ss.next(price=70)
    ss.next(price=60)
    ss.next(price=75)
    ss.next(price=85)
