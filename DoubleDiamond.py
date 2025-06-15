n=int(input("Enter number: "))
for i in range(2*n):
    if i < n:
        spaces=n-(i+1)
        stars=(2*i)+1
        print(' ' * spaces,'*' * stars)
    else:
        spaces=i-n
        stars=2*(2*n-1-i)+1
        print(' ' * spaces, '*' * stars)
    