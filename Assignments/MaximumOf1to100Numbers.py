import random
count = 0
maximum_number = 0
for i in range(1,101):
    n = random.randint(1,100)
    if n > maximum_number:
        maximum_number = n
        count += 1
        print(f"The maximum number is {maximum_number} <== update")
    else:
        print(n)
print(f"The number of maximum numbers ={count}")
print(f"The maximum number is {maximum_number}")
    

    
    
   
    



