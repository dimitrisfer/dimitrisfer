#Beginning of the program 

#Asking the user to give three numbers 
a,b,c=input("Give three numbers: ") #In python 2 the input function is used for entering numbers 

# starting the process 
max = a 

if(max < b):
  max = b
#end if

if(max < c):
  max = c
#end if

print("The biggest number between the three is: ", max)

#End of the program
