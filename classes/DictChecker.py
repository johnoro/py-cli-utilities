# Question:
# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

# Hints:

# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.

# AND

# Question:
# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

# Hints:

# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.

class DictChecker:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def printDict(self):
        dict = {}
        for i in range(self.min, self.max + 1):
            dict[i] = i ** 2
        print(dict)

def main():
    dictChecker = DictChecker(1, 3)
    dictChecker.printDict()

    dictChecker = DictChecker(1, 20)
    dictChecker.printDict()

if __name__ == "__main__":
    main()
