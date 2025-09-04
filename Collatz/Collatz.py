"""
Collatz. Todo numero entero positivo llegara a 1.
Al divir por 2 si es par, si no por 3 y sumarle 1.
"""

def collatz(n):
    if n == 1:
        return print(n)
    elif n % 2 == 0:
        print (n//2)
        n = collatz(n//2)
    else:
        print (3*n + 1)
        n = collatz(n=3*n + 1)

n = int(input("Enter a positive integer: "))
collatz(n)
