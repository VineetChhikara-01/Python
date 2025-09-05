'''
file modes:
r-reading(default)
w-write(create a file if don't exists)
a-append (will also create new file )
'''
# reading a file
f=open("file.txt")
# read returns all the data of the file
# r=f.read()
# print(r)

# readline returns a string i.e a line and calling it again and again it returns next line 
line=f.readline()
print(line)

# readlines returns the list of all lines
lines=f.readlines()
print(lines)

f.close()

# writing a file
g=open("file1.txt",'w')

# the write function will delete all the existing data of the file and add new data only
g.write("hello world 12")

g.close()

# append mode
h=open("append.txt","a")

# by using append mode we can use write function to add the data to existing data in the file
h.write("hello ")
h.write("world ")
h.write("vineet")

h.close()