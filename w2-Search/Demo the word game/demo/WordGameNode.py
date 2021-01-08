from Node import Node
from string import ascii_lowercase

valid_words = []

def read_dictionary(filename, length):
    
    global valid_words
    valid_words = []
    f = open(filename)
    lines = f.read().strip()
    li = lines.split()

    for w in li:
        if len(w) == length and w.islower() and w not in valid_words and "'" not in w:
           valid_words.append(w)
    
class WordGameNode(Node):
   def __init__(self, name, parent = None):
      # Ensure lowercase letters (no digits or special chars)
      for letter in name:
         assert letter in ascii_lowercase

      self.name = name
      self.parent = parent
      self.valid_words = None

   def __str__(self):
      return self.name
   
   def get_parent(self):
      return self.parent

   def get_children(self):
      global valid_words
      word = self.name
      child_words = []
   
      i = 0
      for let in word:
         for n in range(26): # to get index of each letter in alphabet
            letter = chr(ord("a") + n) # to convert each index to a letter
            if let != letter:# if current letter isn't equal to new letter 
               word1 = word[:i] + letter + word[i+1:] # iteration of letters
               if word1 in valid_words: # check to see if in valid words
                  child_words.append(WordGameNode(word1, self)) # if it is append as wordgamenode
         i+=1

      return child_words

   def get_path(self):
      path = [self]
      while self.parent != None:
         path.append(self.parent)
         self = self.parent
      return path
