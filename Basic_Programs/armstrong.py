def armstrong(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    power = len(digits)
    total = sum(d ** power for d in digits)
    return n == total

# Example usage
n = int(input("Enter a number: "))
if armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
