from Node import Node
from string import ascii_lowercase

class WordGameNode(Node):
   def __init__(self, name, parent = None):
      # Ensure lowercase letters (no digits or special chars)
      for letter in name:
         assert letter in ascii_lowercase
      self.name = name
      self.parent = parent

   def __str__(self):
      return self.name

   def get_children(self):
      # all one letter mutations of the word
      #len_alphabet = 26

      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      word = self.name

      child_words = []
   
      i = 0
      for let in word:
         for n in range(26): # to get index of each letter in alphabet
            letter = chr(ord("a") + n) # to convert each index to a letter
            if let != letter: # if current letter isn't equal to new letter 
               child_words.append(WordGameNode(word[:i] + letter + word[i+1:])) #then append to list and return as WordGameNodes
         i+=1



      return child_words # Need to return a list of WordGameNode objects.

   def get_path(self):
      # insert code here
      return path
