
def max_profit_03(prices):
    if not prices:
        return 0

    n = len(prices)
    max_profit_1 = [0] * n  # max profit after the first transaction
    max_profit_2 = [0] * n  # max profit after the second transaction

    min_price_1 = prices[0]  # min price before the first transaction
    min_price_2 = prices[0]  # min price before the second transaction

    for i in range(1, n):
        # Update max profit after the first transaction
        max_profit_1[i] = max(max_profit_1[i - 1], prices[i] - min_price_1)
        # Update min price before the first transaction
        min_price_1 = min(min_price_1, prices[i])

        # Update max profit after the second transaction
        max_profit_2[i] = max(max_profit_2[i - 1], prices[i] - min_price_2)
        # Update min price before the second transaction
        min_price_2 = min(min_price_2, prices[i] - max_profit_1[i - 1])

    # Return the maximum profit after two transactions
    return max_profit_2[-1]

print(max_profit_03([3,3,5,0,0,3,1,4]))





