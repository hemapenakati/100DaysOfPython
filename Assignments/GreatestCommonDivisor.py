n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
d=min(n,m)
while n%d!=0 or m%d!=0:
    d=d-1
print("The G.C.D of two numbers is ",d)