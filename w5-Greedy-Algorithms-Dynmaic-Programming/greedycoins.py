def make_sum(total, coins):
    coins.sort(reverse=True)
    used_coins = [0] * len(coins)
    
    for i, coin in enumerate(coins):
        while total >= coin:
            used_coins[i] += 1
            total -= coin
    
    return used_coins # a list indicating which coins are used to make the sum.
 