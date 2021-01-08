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
