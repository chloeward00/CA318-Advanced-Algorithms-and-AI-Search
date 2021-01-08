#
#   In this exercise, find the most value you can get from items which you will fit into a knapsack
#    using dynamic programming.
#
#   return the memo that you create as a result
#
import math # for use in kapsack function
def getVal(item):
	return item.value/item.weight # function to help sort


def ks_greedy(capacity, items):
	assert capacity >= 0
	total_value = 0
	items.sort(key=getVal, reverse=True)

	for item in items:
		while capacity >= item.weight:
			total_value += item.value
			capacity -= item.weight

	return total_value
	
def dp_knapsack(capacity, items):
	assert capacity >= 0
	
	memo = [math.inf] * (capacity+1)
	
	memo[0] = 0

	for item in range(1, len(memo)):
	    
	    
		memo[item] = ks_greedy(item, items) # referring back to ks_greedy function from earlier

	return memo

#
#   normally, you would return memo[capacity] at this point, but in this exercise, you just return the memo.
#