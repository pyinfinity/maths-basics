class maths:
    def factorial(self):
        factor = 1
        for a in range(1,self+1):
            factor = a * factor
        print(f'The factorial of {self} is {factor}')

    def square_root(self):
        for a in range(1,self//2):
            if self == a*a:
                print(f"The square root of {self} is {a}")
            else:
                pass

b = maths.factorial(5)
c = maths.square_root(81)
print("Note: If not square root is printed then system is not able to find one!")