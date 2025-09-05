# # list is the collection of data elements
# # [] are use to declare list 
# # properties : ordered ,indexed ,muteable and can contain duplicate values
# lis=[]
lis1=[67,6,3,7,9,0]
# #methods :
# we can slice list as like strings
# print(lis1)
# lis1.sort()
# print(lis1)
# lis1.append(3)
# print(lis1)
# lis1.reverse()
# print(lis1)
# lis1.remove(3)
# print(lis1)
# lis1.insert(3,"vineet")
# print(lis1)
# lis1.pop(0)
# print(lis1)
# lis1.clear()
# print(lis1)

# # tuples 
# # () are use to declare list 
# # properties : ordered ,indexed ,inmuteable and can contain duplicate values
# tup=() #empty tuple
# tup3=(1,) #tuple with one element only
# tup1=(4,5,2,"ndfsjn",5,4,0)
# # #methods :
# print(tup1.count(4)) #count the occurence of value
# print(tup1.index(4)) #returns the index of first value 

# # sets
# # {} are use to declare list 
# # properties : unordered ,unindexed ,muteable and can't contain duplicate values
# set0=set() #empty set
# set1={0,1}
# set2={3,5,1,"vineet"}
# # #methods :
# print(set2) 
# print(set1)
# set2.update(set1)#adds the set1 elements to set2
# print(set2)#
# set2.remove(3)#remove the value from the set
# print(set2)#
# set2.add(78)#add the value to set
# print(set2)#
# print(set2.union(set1))#returns the union 
# print(set2.intersection(set1))# returns the intersection
# print(set2.issubset(set1))# returns true or false
# print(set1.issubset(set2))#returns true or false
# print(set2.issuperset(set1))#returns true or false
# many more methods

# # dictionary are collection of key value pair
# # {} are use to declare list 
# # properties : ordered ,indexed ,muteable and can't contain duplicate keys
# dict={} #empty dictionary
# dict2 ={"rahul":100,"vineet":100,"key":50}
# # #methods :
# print(dict2)
# dict2.update({"key2":"value"}) #update the value of the key and adds the key and value if didn't exist
# print(dict2)
# print(dict2.keys()) #returns the keys of dict
# print(dict2.values()) #returns the values of the keys of dict
# print(dict2.get("key")) #retuens the value of key otherwise returns none if key is not present
# print(dict2["rahul"]) # returns the value of key if present otherwise returns error
# print(dict2.items())#return the items i.e key value pair of dictionary
# #many more