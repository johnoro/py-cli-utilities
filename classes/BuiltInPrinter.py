# Question:
#     Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
#     Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
#     And add document for your own function
    
# Hints:
#     The built-in document method is __doc__

class BuiltInPrinter:
    def __init__(self):
        pass

    def printBuiltIn(self, builtIn):
        print(builtIn.__doc__)
    
    def printBuiltInList(self, builtInList):
        for builtIn in builtInList:
            print()
            print(builtIn.__name__, "-->")
            print()
            self.printBuiltIn(builtIn)
            print()
    

def main():
    builtInPrinter = BuiltInPrinter()
    builtInPrinter.printBuiltInList([abs, int, input])

if __name__ == "__main__":
    main()
