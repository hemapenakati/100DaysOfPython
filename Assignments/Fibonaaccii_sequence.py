n = int(input("Enter the number: "))
num = 1
prev_num = 0
print(prev_num)
print(num)
for i in range(0,n+1):
    next_num = prev_num + num
    prev_num = num
    num = next_num
    print(next_num)