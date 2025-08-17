n = int(input("Enter a number: "))
factorial = 1
steps = []

for i in range(1, n+1):
    factorial *= i
    steps.append(str(i))  # keep factors in correct order

# Join the steps with '*' for clarity
steps_str = " * ".join(steps)

print(f"Factorial of {n}! is {steps_str} = {factorial}")
