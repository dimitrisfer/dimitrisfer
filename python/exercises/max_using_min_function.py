#func1
def min(a,b,c):
    first = (a + b - abs(a-b)) / 2
    return (first + c - abs(first - c)) / 2
#end func1

#func 2
def max(a,b,c):
    sum = a+b+c
    minimum = min(a, b, c)
    mid = min(a+b,b+c,a+c) - minimum
    max = sum - mid - minimum
    return max
#end func 2

#main()
print(max(1,0,10))
