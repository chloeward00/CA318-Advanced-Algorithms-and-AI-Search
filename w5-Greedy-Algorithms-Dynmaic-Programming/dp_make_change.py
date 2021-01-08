import math
def dp_make_change(amount,coins): 
      
    # memo[i] will be storing the minimum  
    # number of coins required for i value.  
    # memo[amount] will have result 
    m = len(coins)
    memo = [0 for i in range(amount + 1)] 
    memo[0] = 0
  
    # initialise all table values as inf 
    for i in range(1, amount + 1): 
        memo[i] = math.inf
  
    for i in range(1, amount + 1): 
        for j in range(m): 
            if (coins[j] <= i): 
                sub = memo[i - coins[j]] 
                if (sub != math.inf and sub + 1 < memo[i]): 
                    memo[i] = sub + 1
    return memo