class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        count  = 0
        for i in costs:
            if coins-i >= 0:
                coins = coins - i
                count += 1
            else:
                return count
        return count
        