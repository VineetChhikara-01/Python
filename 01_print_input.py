# print() method
print("hello world") #print any content,data enclosed in the ' or "
print('''multi line ''') #to print multi line
a=34
print(a) #to print any variable 
b ="vineet"
c="chhikara" 
print(c,b) #we can print multiple variable by using either " , "
print(c+b) # or by using " + " between the varibles but the "+" will only be used when the variables are of same type
# sequence character
# the following sequence characters are used in print method or strings
# \n - new line
# \t - add space
# \\ - add backslash ( \ )
# \' or \" - add ' or "


# variables
#in python we don't need to specify the type of the variable ,it automatically detects the type of the variable

x=65 #int data type
y=758.5 #float data type
z="vineet" #string data type NOTE:string are enclosed between the 'string',"string" or '''string''' 
u=True #boolean data type
#there are rules to name the variables like we cannot start the variable by any interger value or by any special character 
# we can use underscroll in the variable name

#type() method
#we can know the type of the variable by using the type() method
print(type(x))
print(type(y))
print(type(z))
print(type(u))

# input() method
#it is used to get input from the user 
#syntax:
#variable_name = input("message to be displayed while taking input")
inp = input("enter input")
# by default in python the input given is always considered as the string data type 
# we can typecast the input data according to our needs
inp2 = int(input("message")) #input data will be converted to the int data type
print(inp2)
