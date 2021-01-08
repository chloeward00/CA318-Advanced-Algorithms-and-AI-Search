def read_dictionary(filename, length):
    
    # your code here
    words = []
    f = open(filename)
    lines = f.read().strip()
    li = lines.split()

    #eturn lines # a list of the words in the dictionary which comprise only lower case letters and are of the correct length

    for w in li:
        if len(w) == length and w.islower() and w not in words and "'" not in w:
            words.append(w)
    return words