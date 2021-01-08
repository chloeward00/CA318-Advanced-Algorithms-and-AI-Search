def longest_common_subsequence(s, t, memo):

    s_index = len(s)
    t_index = len(t)

    index = memo[s_index][t_index] 

    lcs = [""] * (index+1) 
    lcs[index] = "" 
  

    i = len(s)
    j = len(t)
    
    while i > 0 and j > 0: 
  
        if s[i-1] == t[j-1]: 
            lcs[index-1] = s[i-1] 
            i-=1
            j-=1
            index-=1
  
        
        elif memo[i-1][j] > memo[i][j-1]: 
            i-=1
        else: 
            j-=1
  
    result = "".join(lcs)
    return result