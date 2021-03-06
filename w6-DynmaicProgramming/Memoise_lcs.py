def recursive_lcs(s, s_index, t, t_index, memo):
    if s_index == len(s) or t_index == len(t):
        return 0
    else:
        if memo[s_index][t_index] != -1:
            return memo[s_index][t_index]
        else:
            move_both = recursive_lcs(s, s_index+1, t, t_index+1, memo) + 1 if s[s_index] == t[t_index] else 0
            move_s = recursive_lcs(s, s_index+1, t, t_index, memo)
            move_t = recursive_lcs(s, s_index, t, t_index + 1, memo)
            
            memo[s_index][t_index] = max([move_both, move_s, move_t])
            return memo[s_index][t_index]


def longest_common_subsequence(s, t):
    # Create an appropriately sized memo
    # Initialised to -1
    memo = [ [-1 for i in range(len(t))] for j in range(len(s))]
    
    # Call the recursive function ... it will build up the memo.
    lcs = recursive_lcs(s, 0, t, 0, memo)
    
    return memo # now, return the memo


def main():

    print(longest_common_subsequence('TAGTCACG','AGACTGTC'))



if __name__ == '__main__':
    main()