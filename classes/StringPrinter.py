# Question:
# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

class StringPrinter:
    def __init__(self):
        pass

    def printString(self, string):
        print(string)

    def printStringList(self, stringList):
        for string in stringList:
            self.printString(string)

    def printStringListWithMaxLen(self, stringList):
        maxLen = 0
        for string in stringList:
            if len(string) > maxLen:
                maxLen = len(string)
        for string in stringList:
            if len(string) == maxLen:
                self.printString(string)

def main():
    stringPrinter = StringPrinter()
    stringPrinter.printStringListWithMaxLen(["abc", "abcd", "abcde"])
    print('----------------')
    stringPrinter.printStringListWithMaxLen(["abc", "abcd", "abcd", "ab"])

if __name__ == "__main__":
    main()
