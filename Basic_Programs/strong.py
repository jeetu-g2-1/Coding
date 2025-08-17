def factorial(x: int) -> int:
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def strong(n: int) -> bool:
    original = n
    total = 0
    while n > 0:
        digit = n % 10
        total += factorial(digit)
        n //= 10
    return total == original
n = int(input("Enter a number: "))
if strong(n):
    print("Strong Number")
else:
    print("Not a Strong Number")
