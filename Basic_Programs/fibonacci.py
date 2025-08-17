def fibonacci(n: int):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
n = int(input("Enter how many terms: "))
fibonacci(n)
