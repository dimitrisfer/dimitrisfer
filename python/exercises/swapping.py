#Function to swap the numbers
def swap(x, y):
    temp = x    
    x = y
    y = temp
    print(x, y)
#main()
x=float(input("Give the first: "))
y=float(input("Give the second: "))
swap(x, y)
#end
