from Node import Node
from string import ascii_lowercase,punctuation

valid_words = None



def isvalid_word(word,length):
     word = word.strip()
     if word.isupper() or len(word) != length:
             return False
     for w in word:
             if w in punctuation or w not in ascii_lowercase:
                     return False
     return True
     
def read_dictionary(filename,length):
     with open(filename) as f:
             l = [word.strip() for word in f.readlines() if isvalid_word(word,length)]

     return l


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
            self.depth = 0

     def __str__(self):
            return self.name



     def get_children(self):
            # all one letter mutations of the word
            child_words = []
            word = self.name
            for j in range(len(word)):
                 tmp = [("".join(word[:j]) + ascii_lowercase[i] + "".join(word[j+1:])) for i in range(len(ascii_lowercase)) if ascii_lowercase[i] != word[j]]
                 child_words += tmp 
            
            return [WordGameNode(wrd,self) for wrd in list(set(child_words)&set(valid_words))]

     def get_parent(self):
         return self.parent


     def out_place(self,goal):

        start = self.name
        goal = goal.name

        count = 0
        for i in range(len(self.name)):

            if start[i] != goal[i]:

                count += 1

        return count

     def get_path(self):
            path = [self]

            while self.get_parent() != None:
                 path.append(self)
                 self = self.get_parent()
                 
            return path
