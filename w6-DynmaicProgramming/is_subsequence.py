def is_subsequence(word1, word2):


    word1 = list(word1)
    for letter in word2:
        if word1 and word1[0] == letter:
            word1.pop(0)

    return not word1


