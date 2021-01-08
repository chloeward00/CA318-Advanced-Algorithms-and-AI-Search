def create_b(bd):
	d = {}
	for i in range(9):
		d[bd[i]] = (i//3,i%3)

	return d

def h(start,goal):
	s = create_b(start)
	g= create_b(goal)
	
	distance = 0
	for i in range(9):
		n = start[i]	
		gi = str(goal.index(n))	
		if i != int(gi) and n != " ":
			k = goal[int(gi)]
			distance += (abs(g[k][0] - s[n][0])) + abs(g[k][1] - s[n][1])
	return distance