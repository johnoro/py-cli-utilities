# - Simple Calculator
# to add proper order of operations, 
# a stack could be used 
# along with some priority rules stored with each operator
# (plus a rule to read parentheses)

import sys

operators = { 'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/' }

def calc(operand1, operator, operand2):
    if operator == operators['add']:
        return operand1 + operand2
    if operator == operators['subtract']:
        return operand1 - operand2
    if operator == operators['multiply']:
        return operand1 * operand2
    if operator == operators['divide']:
        return operand1 / operand2
    print("Invalid operator; current operators are: " + ", ".join(operators.values()))

def calc_helper(eq_it, total):
    while True:
        try:
            op = next(eq_it)
            operand = int(next(eq_it))
            total = calc(total, op, operand)
        except:
            return total

intro = 'Please type your equation with spaces in between each operator and operand.\n' + f'Please note that operations are executed in the order they come.'

def main():
    args = sys.argv[1:]
    print(intro)
    if not args:
        args = input('Please enter your equation: ').split(' ')
    eq_it = iter(args)
    total = int(next(eq_it))

    total = calc_helper(eq_it, total)
    print(total)

if __name__ == '__main__':
    main()
