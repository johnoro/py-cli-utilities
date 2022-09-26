# Question:
# Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

# Hints:

# Use % operator to check if a number is even or odd.

class EvenOddChecker:
    def __init__(self):
        pass

    def check(self, number):
        if number % 2 == 0:
            print(f"{number} is an even number")
        else:
            print(f"{number} is an odd number")

def main():
    evenOddChecker = EvenOddChecker()
    evenOddChecker.check(2)
    evenOddChecker.check(3)

if __name__ == "__main__":
    main()
