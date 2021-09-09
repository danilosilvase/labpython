# How would you code a recursive function to print a certain Fibonacci number?

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

z = 10
for x in range(z):
    print(fibonacci(x))