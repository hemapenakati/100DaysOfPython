# WAP to execute the following
#1
#12
#123
#1234
#12345
'''n = int(input("Enter any number: " ))
s = ""
for i in range(1,n+1):
    s = s + str(i)
    print(s)'''
#WAP to print whether the number is prime number or not?
'''n = int(input("Enter any number: "))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print("It is a prime number")
else:
    print("It is not a prime number")'''
#WAP to print the fibonaaccii sequence of numbers
n = int(input("Enter any number:"))
num = 1
prev_num = 0
print(prev_num)
print(num)
for i in range(0,n+1):
    next_num = prev_num + num
    prev_num = num
    num = next_num
    print(next_num)

