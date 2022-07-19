#we have created an object maths which can perform a few simple mathematical calculations like factorial, square root, sum of first n consecutive numbers etc
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
    def sum_first_n_consq_num(self):
        sum_n = 0
        for a in range(self):
            a = a + 1
            sum_n += a
        print(f"The sum of first {self} consecutive numbers is {sum_n}")

maths.factorial(5)
maths.square_root(81)
maths.sum_first_n_consq_num(8)
print("Note: If not square root is printed then system is not able to find one!")
