def check_path(path):
    # return true/false depending on whether the path is valid or not.
    # node starts at the end of the path
    # compare child and parent nodes so it will look like child[i], parent[i+1]
    # get the list of moves of the parent node
    # check if the child is in of those possible plays, if it is return true otherwise return false 
    # check ur drawing
    
    count = 0
    for i in range(len(path) - 1):
        child = path[i]
        parent = path[i + 1]
        
        list_of_plays = parent.get_moves()          # list of possible plays
        if child not in list_of_plays:              # so if the current/child play is not in the parents possible list, that path is wrong ie return false and loop finishes 
            return False

    return True                                     # returns true if the loop is successful ie path is correct
    