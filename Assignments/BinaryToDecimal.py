# Ex-binary to decimal
n=input("Enter the binary number:")
x=len(n)-1
s=0
for i in range(x+1):
      s=s+(int(n[x-i])*2**i)
print(s)

# Ex- decimal to binary
n = int(input("Enter the decimal number:"))
bin=""
while n > 0:
      rem=n%2
      n=n//2
      bin=str(rem)+bin
print(bin)
