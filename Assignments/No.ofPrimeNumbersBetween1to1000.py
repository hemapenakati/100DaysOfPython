n = int(input("Enter any number:"))
counter = 0
for i in range(1,n+1):
    count = 0
    
    for j in range(1,i+1):
        if i%j == 0:
            count = count + 1
            
    if count == 2:
        counter = counter + 1
        print(i)
print("No.of prime number are ",counter)
   
            
    