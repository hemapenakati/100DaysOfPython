'''n = int(input("Enter any number:"))
s = 0
for i in range(1,n):
    if n%i == 0:
        s = s + i
if s == n:
    print("{} is a perfect number".format(n))
else:
    print("{} is not a perfect number".format(n))'''
#while loop
n = int(input("Enter any number:"))
s = 1
sum = 0
while s < n:
    if n%s == 0:
        sum = sum + s
    s = s + 1
if sum == n:
    print("{} is a perfect number".format(n))
else:
    print("{} is not a perfect number".format(n))
        
    

    