def longest_common_subsequence(s, t):
    # Create an appropriately sized memo
    # Initialised to -1
    memo = [ [-1 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
    
    # Call the recursive function ... it will build up the memo.

    for row in range(len(s)+1): # first row as all 0's
        memo[row][0] = 0

    for col in range(len(t)+1): # first col as all 0's
        memo[0][col] = 0

    

    for s_index, x in enumerate(s):
        for t_index, y in enumerate(t):
            if x == y:
                memo[s_index+1][t_index+1] = memo[s_index][t_index] + 1
            else:
                memo[s_index+1][t_index+1] = max(memo[s_index+1][t_index], memo[s_index][t_index+1])
 
    # read a substring from the matrix
    return memo # now, return the memo

def main():

    print(longest_common_subsequence("TAGTCACG","AGACTGTC"))


if __name__ == '__main__':
    main()