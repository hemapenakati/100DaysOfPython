# WAP to check whether it is a prime number or not
n = int(input("Enter any number:"))
count = 0
for i in range(1,n+1):
    n1 = n % i
    if n1 == 0:
        count = count + 1
if count == 2:
    print("Prime number")
else:
    print("Not a prime number")


















