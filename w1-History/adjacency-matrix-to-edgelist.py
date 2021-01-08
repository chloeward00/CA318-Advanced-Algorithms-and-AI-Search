def make_edge_list(adjacency):
    """ this function create an edge list representation of a graph using the supplied adjacency matrix
    """
    # Maybe start with an empty edge_list
    edge_list = []
    
    # Insert code here
    alpha = []
    for i in range(len(adjacency)):
        letter = chr(ord("A") + i)
        alpha.append(letter)

    for line in adjacency:
        temp = []
        for item in range(len(line)):
            if line[item] == 1:
                temp.append(alpha[item])
        edge_list.append(temp)
    
    return edge_list