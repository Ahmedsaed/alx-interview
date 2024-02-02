#!/usr/bin/python3
"""Making Change"""


def makeChange(coins, total):
    """
        determine the fewest number of coins
        needed to meet a given amount total
    """
    if total <= 0:
        return 0

    total_coins = 0
    for coin in sorted(coins, reverse=True):
        if coin > total:
            continue
        elif total == 0:
            break

        total_coins += (total // coin)
        total -= (total // coin) * coin

    if total != 0:
        return -1
    else:
        return total_coins
