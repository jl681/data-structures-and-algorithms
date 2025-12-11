# time complexity O(n^2) = o(n) for loop and o(n) for max_iterations
# def max_profit(prices):
#     result = []
#     for i in range(len(prices) - 1):
#         remaining = prices[i+1:]
#         result.append(max(remaining) - prices[i])
#     if max(result) <= 0:
#         return 0
#     return max(result)

def max_profit_01(prices):
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        current_profit = price - min_price
        max_profit = max(current_profit, max_profit)
        min_price = min(price, min_price)
    return max_profit



