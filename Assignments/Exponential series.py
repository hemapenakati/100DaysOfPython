n = int(input("Enter any number:"))
e_power_x=(1+1/n)**n
for i in range(1,n+1):
    e_power_x = e_power_x + i
    print("The value of e power x is ",e_power_x)
