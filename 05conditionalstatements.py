# conditional statements 
# these statements are used to check the condition,if true perform the given statement
# if-else satements are conditional statements
# syntax:
# if(condition):
#   statements to perform if the condition is true
# else:(optional)
#   statement to perform if the condition is false 
a=5
b=6
if(a>b):
    print(a)
else:
    print(b)

# nested if-else
c=9
if(a>b):
    if(a>c):
        print(a)
    else:
        print(c)
else:
    if(b>c):
        print(b)
    else:
        print(c)

# elif 
if(a>b): 
    print(a)
elif(b>c): # it will be executed if the above if (or elif present ) is false 
    print(b)
else: #this will be executed if all if and elif conditions are true
    print(c)

# we can use logical,comparision operators in the conditional statements
if(a>b and b==c or c<100):
    print("lorem")