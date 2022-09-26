# Question:
# Define a function that can convert a integer into a string and print it in console.

# Hints:

# Use str() to convert a number to string.

class IntToStringConverter:
    def __init__(self):
        pass

    def convert(self, number):
        print(str(number))

def main():
    intToStringConverter = IntToStringConverter()
    intToStringConverter.convert(123)

if __name__ == "__main__":
    main()
