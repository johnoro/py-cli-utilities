# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# Hints
# In case of input data being supplied to the question, it should be assumed to be a console input.

class WordFrequencyCalculator:
    def __init__(self):
        self.wordFrequency = {}
    
    def addWord(self, word):
        if word in self.wordFrequency:
            self.wordFrequency[word] += 1
        else:
            self.wordFrequency[word] = 1
    
    def printWordFrequency(self):
        for word, frequency in self.wordFrequency.items():
            print(f'{word}:{frequency}')
    
    def printWordFrequencySorted(self):
        for word, frequency in sorted(self.wordFrequency.items()):
            print(f'{word}:{frequency}')
            
def main():
    wordFrequencyCalculator = WordFrequencyCalculator()
    s = input("Enter a sentence: ")
    for word in s.split(" "):
        wordFrequencyCalculator.addWord(word)
    wordFrequencyCalculator.printWordFrequencySorted()

if __name__ == "__main__":
    main()
