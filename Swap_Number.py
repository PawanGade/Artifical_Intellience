# Python code to swap two numbers

x = 8
y = 36

print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

# Swap code
x = x + y 
y = x - y 
x = x - y 

print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)


"""
Output -

Before swapping: 
Value of x :  8  and y :  36
After swapping: 
Value of x :  36  and y :  8

"""
