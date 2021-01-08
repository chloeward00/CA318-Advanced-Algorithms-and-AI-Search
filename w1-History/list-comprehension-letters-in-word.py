def sol(word, letter):
    b = [w for w in word if letter not in w]
    return(b)