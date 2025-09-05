# loops
# two types of loops : 1 for loop ,2 while loop 
# foor loops syntax
# for i in range(start,end,jump):
    # statement to execute
# while(condition):
    # statement to execute 
    # NOTE to give the end condition of the loops so that it don't enter infinite loop

# for loops
# use with range funtion
# for i in range(1,10,2):
#     print(i)

# # use with list,tuple and string
# list=[1,4,"vineet",990]
# tuple=(1,4,8,5,"chhikara")
# string="string"
# for i in list:
#     print(i)
# for i in tuple:
#     print(i)
# for i in string:
#     print(i)

# # we can also use break(to exit loop),continue(to skip the following statements for the iteration) and pass(to do nothing)
# for i in range(4):
#     if(i==3):
#         break
#     if(i==2):
#         continue
#     print(i)

set={"vineet":"vineet",2:"rahul",5:"jatin",4:"shubham"}
for i in set:
    print(i)
# # WHILE LOOPS
# i=0
# while(i<5):
#     i += 1 
#     print(i)
# # using while loops in list
# i=0
# while(i<len(list)):
#     print(list[i])
#     i+=1
