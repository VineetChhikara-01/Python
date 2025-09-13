# strings is the data type 
# we can use and manipulate strings in many ways

# concatinate two or many strings using " + "
a="vineet"
b="chhikara"
c=a+b #concatinated a and b
print(c)

# we can check any character or string present in the string 
# by using the "in"
# syntax: string1 in string2
print(a in b)
#we can slice the values of string
# syntax:
# variable_name[<starting index>:<stop_index>:<jump/skip index by value>]
print(c[0:6]) #start from 0 till 6 excluding 6th
print(c[-5:-2]) #start from -5th till -2 (we can use negative index from last)
print(c[3:-1:2]) #using both positive and negative index by skipping 2 indexes
print(c[4:]) #start from 4th till last of the string
print(c[:9]) #start from 0th index till 9th (excluding 9)

# we can also get specific character of the string by giving the index of the character of the string
print(c[5])

#methods NOTE these functions do not change the existings string but returns new value or string
print(len(c))# gives the length of string
print(c.endswith("ara")) #gives true or false wheather the string endswith the provided substring
print(c.startswith("vin")) #gives true or false wheather the string startswith the provided substring
print(c.capitalize()) #capitalises the first letter of the string
print(c.count("a")) #counts the number of occurence of the character in the string
print(c.lower()) #returns the string with all character with lowercase
print(c.upper()) #returns the string with all character with uppercase
print(c.find("ara")) #returns starting index of occurence of the substring present in the string
print(c.replace("ee","i")) #replaces the oldword present in string with the new world
print(c.strip()) #strip removes blankspace from starting and last ,also we can also use lstrip(starting space),rstrip(end space)