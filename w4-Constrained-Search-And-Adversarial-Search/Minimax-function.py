def minimax (tree): 
	r = tree.root
	d = 0
	return _minimax(r,d)


def _minimax(r,d):
	#base case
	if r.is_terminal():  
		return r.evaluation() 
	  
	if d % 2 == 0: 
		return max(_minimax(r.left,d+1),_minimax(r.right,d+1),_minimax(r.mid,d+1)) 
	
	else:
		return min(_minimax(r.left,d+1),_minimax(r.right,d+1),_minimax(r.mid,d+1))