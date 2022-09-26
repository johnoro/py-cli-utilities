# CLI Utilities

A number of simple CLI python scripts primarily for demonstrative purposes.

---

## **How to run**

If you'd like the most simple way forward, run `python functions/main.py` and follow the prompts.

To use, run src/main.py with the desired script name as an argument. For example, to run the hello world script, run `python functions/main.py leap_year 40`. You may also run the script directly, e.g. `python functions/leap_year.py 40`. You may also omit arguments (file/function names and their arguments included) and you will be prompted for them.

For the newly added classes section, run `python classes/main.py` and follow the prompts. No CLI arguments are supported for the specific class scripts, but you can still run `python classes/main.py <class_name>` or `python classes/ <class_name>.py` to run the class script directly.

---

## **Functional Scripts**

Note that the actual outputs have been transformed primarily into more readable print statements.

- ### _absolute_value.py_

  Returns the absolute value of a {number} (also can take a list of numbers).

  Usage: python absolute_value.py {number}

  Example: python absolute_value.py -5

  Output: 5

---

- ### _calculator.py_

  A simple calculator.

  Usage: python calculator.py {number} {operator} {number} ...

  Operators: +, -, \*, /, ^

  Example: python calculator.py 5 + 5

  Output: 10

  Example: python calculator.py 5 ^ 2

  Output: 25

  Example: python calculator.py 5 \* 5 + 5

  Output: 30

  Example: python calculator.py 5 + 5 / 5

  Output: 2 _Note that the order of operations is not followed._

---

- ### _copy.py_

  Copies a list.

  Usage: python copy.py {list}

  Example: python copy.py [1, 2, 3]

  Output: [1, 2, 3]

  Example: python copy.py [1, 2, 3, [4, 5]]

  Output: [1, 2, 3, [4, 5]]

---

- ### _count_same_first_last.py_

  Counts the number of strings in a list that have the same first and last element.

  Usage: python count_same_first_last.py {list}

  Example: python count_same_first_last.py ['egregious', 'test', 'local']

  Output: 2

  Example: python count_same_first_last.py ['racecar', 'test', 'local']

  Output: 3

---

- ### _fibonnaci.py_

  Returns the nth fibonnaci number (also can take a list of numbers).

  Usage: python fibonnaci.py {number}

  Example: python fibonnaci.py 5

  Output: 5

  Example: python fibonnaci.py 10

  Output: 55

  Example: python fibonnaci.py 5 10

  Output: 5, 55

---

- ### _is_empty.py_

  Returns whether a list is empty.

  Usage: python is_empty.py {list}

  Example: python is_empty.py []

  Output: True

  Example: python is_empty.py [1, 2, 3]

  Output: False

---

- ### _leap_year.py_

  Returns whether a year is a leap year (also can take a list of years).

  Usage: python leap_year.py {year}

  Example: python leap_year.py 2000

  Output: True

  Example: python leap_year.py 2001

  Output: False

---

- ### _max_of_three.py_

  Returns the maximum of three numbers.

  Usage: python max_of_three.py {number} {number} {number}

  Example: python max_of_three.py 1 2 3

  Output: 3

  Example: python max_of_three.py 3 2 1

  Output: 3

  Example: python max_of_three.py 1 3 2

  Output: 3

---

- ### _multiply_numbers.py_

  Multiplies a list of numbers.

  Usage: python multiply_numbers.py {list}

  Example: python multiply_numbers.py [1, 2, 3]

  Output: 6

---

- ### _prime.py_

  Returns whether a number is prime (also can take a list of numbers).

  Usage: python prime.py {number}

  Example: python prime.py 5

  Output: True

  Example: python prime.py 10

  Output: False

  Example: python prime.py 5 10

  Output: True, False

---

- ### _remove_duplicates.py_

  Removes duplicates from a list.

  Usage: python remove_duplicates.py {list}

  Example: python remove_duplicates.py [1, 2, 3, 1, 2, 3]

  Output: [1, 2, 3]

---

- ### _reverse_string.py_

  Reverses a string.

  Usage: python reverse_string.py {string}

  Example: python reverse_string.py 'hello'

  Output: 'olleh'

---

- ### _sum_numbers.py_

  Sums a list of numbers.

  Usage: python sum_numbers.py {list}

  Example: python sum_numbers.py [1, 2, 3]

  Output: 6
