from Node import Node
from string import ascii_lowercase
from read_dictionary import read_dictionary

valid_words = None

class WordGameNode(Node):
   def __init__(self, name, parent = None):
      # Ensure lowercase letters (no digits or special chars)
      for letter in name:
         assert letter in ascii_lowercase

      global valid_words
      if valid_words == None or len(valid_words) != len(name):
         # We only need to examine words which have the same length as our word (self.name)
         valid_words = read_dictionary("/etc/dictionaries-common/words", len(name))
      self.name = name
      self.parent = parent

   def __str__(self):
      return self.name

   def get_children(self):
      lphabet = 'abcdefghijklmnopqrstuvwxyz'
      word = self.name

      child_words = []
   
      i = 0
      for let in word:
         for n in range(26): # to get index of each letter in alphabet
            letter = chr(ord("a") + n) # to convert each index to a letter
            if let != letter:# if current letter isn't equal to new letter 
               word1 = word[:i] + letter + word[i+1:] # iteration of letters
               if word1 in valid_words: # check to see if in valid words
                  child_words.append(WordGameNode(word1)) # if it is append as wordgamenode
         i+=1

      return child_words

   def get_path(self):
      # insert code here
      return path