a=int(input("Give a positive number: "))
if(a<=1):
    result = 1
else:
    result = 1
    for i in range(2, a+1):
        result *= i
print(result)
            
