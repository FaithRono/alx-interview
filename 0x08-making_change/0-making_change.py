#!/usr/bin/python3


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize a list to store the minimum number
    # of coins for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill the dp list
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means we cannot
    # make the total with given coins
    return dp[total] if dp[total] != float('inf') else -1

    # Main file for testing
    if __name__ == "__main__":
        print(makeChange([1, 2, 25], 37))  # Expected output: 7
        print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
