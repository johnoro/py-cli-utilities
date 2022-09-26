# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

# Hints:
# Consider use yield

class IteratorBySeven:
    def __init__(self, n):
        self.n = n
    
    def iterate(self):
        for i in range(self.n):
            if i % 7 == 0:
                yield i

def main():
    iterator = IteratorBySeven(100)
    for i in iterator.iterate():
        print(i)

if __name__ == "__main__":
    main()
