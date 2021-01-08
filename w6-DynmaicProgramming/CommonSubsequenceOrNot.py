def is_common_subsequence(word1, word2,word3):

    word1_copy = list(word1)
    word1 = list(word1)
    word1_copy3 = list(word1)
    for letter in word2:
        if word1 and word1[0] == letter:
            word1.pop(0)
        
    for letter2 in word3:
       if word1_copy and word1_copy[0] == letter2:
            word1_copy.pop(0)

    if len(word1) == 0 and len(word1_copy) == 0:
        return True
    else:
        return False












