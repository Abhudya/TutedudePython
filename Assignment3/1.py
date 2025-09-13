def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
a=(int(input("enter a number:")))
print(f"Factorial of {a} is: {factorial(a)}")