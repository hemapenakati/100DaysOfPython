n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
k=int(input("Enter the third number:"))
l=int(input("Enter the fourth number:"))
d = max(n,m,k,l)
while d%n != 0 or d%m != 0 or d%k != 0 or d%l != 0:
    d = d + 1
print(d)

