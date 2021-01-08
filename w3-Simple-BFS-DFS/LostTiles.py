import sys
def h(start, goal):
    # ensure that start and goal are valid positions
    assert "".join(sorted(start)) == " 12345678" and "".join(sorted(goal)) == " 12345678"
    
    # Work out how many tiles are out of place
    
    num_tiles_out_of_place = 0


    for i in range((len(start))):
        if start[i] != goal[i] and start[i] != " ":
            num_tiles_out_of_place +=1

    return num_tiles_out_of_place
