#First function 
def minimum(a,b,c):
  min = a
  if(min > b):
    min = b
  #end if
  if(min > c):
    min = c
  #end if
  return min 
#Second function 
def maximum(a,b,c):
  max = a
  if(max < b):
    max = b
  #end if
  if(max < c):
    max = c
  #end if 
  return max

#main()
a,b,c = input("Enter three numbers: ")
print(minimum(a,b,c), maximum(a,b,c))
#end main
