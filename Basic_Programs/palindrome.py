n=int(input("Enter a number"))
real=n
# reverse=0
# while n > 0:
#     digit=n%10
#     reverse=(reverse*10)+digit
#     n=n//10
#   print(real,reverse==real,'Palindrome')

def palindrome(a: int) -> bool:
    return str(a) == str(a)[::-1]

n = int(input("Enter a number: "))
if palindrome(n):
    print("Palindrome")
else:
    print("Not a Palindrome")

