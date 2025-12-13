def maxProfit(self, prices: List[int]) -> int:
    left = 0
    max_profit = 0
    current_profit = 0
    while left <= (len(prices) - 2):
        for right in range(left + 1, len(prices)):
            if prices[right] > prices[left]:
                current_profit = prices[right] - prices[left]
            if current_profit > max_profit:
                max_profit = current_profit
        left += 1
    return max_profit


# space complexity - O(1)
# time complexity - O(n^2)

# ===== Optimized Solution =====

def maxProfit(self, prices: List[int]) -> int:
    left = 0
    right = 1
    max_profit = 0

    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1
    return max_profit


# space complexity - O(1)
# time complexity - O(n)
