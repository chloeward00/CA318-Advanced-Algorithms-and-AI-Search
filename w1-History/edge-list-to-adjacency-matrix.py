def make_adjacency_matrix(edge_list):
    """ this function create an adjacency matrix representation of a graph using the supplied edge list
    """
    # Maybe start with an empty adjacency matrix
    adjacency_matrix = []
    
    # Insert code here
    for i in range(len(edge_list)):
        letter = chr(ord("A") + i)
        temp = []
        for lst in edge_list:
            if letter in lst:
                temp.append(1)
            else:
                temp.append(0)
        adjacency_matrix.append(temp)
    
    return adjacency_matrix