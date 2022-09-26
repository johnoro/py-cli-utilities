# Question:
#     Define a class, which have a class parameter and have a same instance parameter.

# Hints:
#     Define a instance parameter, need add it in __init__ method
#     You can init a object with construct parameter or set the value later

class GenericClass:
    def __init__(self, n):
        self.n = n
    
    def __str__(self):
        return str(self.n)
    
def main():
    generic = GenericClass(5)
    print(generic)

if __name__ == "__main__":
    main()
