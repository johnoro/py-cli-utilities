# Question 23
# level 1

# Question:
#     Write a method which can calculate square value of number

# Hints:
#     Using the ** operator

# AND

# Question:
# Define a function which can compute the sum of two numbers.

# Hints:
# Define a function with two numbers as arguments. You can compute the sum in the function and return the value.
  
# AND

# Question:
# Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.

# Hints:

# Use int() to convert a string to integer.
# Question:
# Define a function that can accept two strings as input and concatenate them and then print it in console.
# Hints:
# Use + to concatenate the strings

class Calculator:
    def __init__(self):
        pass
    
    def square(self, n):
        return n ** 2
    
    def sum(self, n1, n2):
        return n1 + n2
    
    def sumString(self, n1, n2):
        return int(n1) + int(n2)
    
    def concatenate(self, s1, s2):
        return int(s1 + s2)

def main():
    calculator = Calculator()
    print(calculator.square(5))
    print(calculator.sum(5, 6))
    print(calculator.concatenate("5", "6"))

if __name__ == "__main__":
    main()
