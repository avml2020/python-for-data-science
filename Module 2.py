#Module 2

#now we will learn about Lists, Tuples, Sets, Dictionaries 
#Tuples are an ordered sequence
#Tuples are expressed as comma separated elements within parentheses
#you can store int,str,float in tuples

a = (1,2,5,5,9,"hi","world",5.9)
print(type(a))

#we can use indexing on tuples
print(a[1])
print(a[5])
print(a[-1])

# we can do slicing also on tuples
#slicing is nothing but geting specific portion out
print(a[0:4])
print(a[4:8])

#we can use len command to get length of a tuple
print(len(a))

#NOTE(very important):Tuples are immutable which means we can't change them
# trying to change 3rd value in a from 5 to 3: you will get an error
#a[2] = 3

#if we want to modify a old tuple we have assign it to a new variable and use some methods while assigning for canges
#example
k = (10,5,7,3,1)
print(k)
b = sorted(k)
print(b)

#A tuple can contain other tuples as well 

a2 = (1,4,("hi",3),5,10,(34,45,("str","tyu")))     
print(a2)

# again we can use indexing on a2 type tuples
# visulaize it as a tree and always give parent branch first and then child
#example i want to get "tyu"

a2[5][2][1]

##################################LISTS#####################################
# it is also a ordered sequence
#A list is represented with square brackets.
#NOTE : In many respects lists are like tuples. One key difference is they are immutable
#Lists can contain strings, floats, integers.We can nest other lists. We also nest tuples and other data structures.


h = [1,4,7,7,(5,"hi"),["tt","rr"],6,8]
print(h)

#we can add new list to the old list elements using extend method
h.extend(["new","list"])
print(h)

#we can use append method to add a new list to the old list
h.append([5,"tyu"])
print(h)

#As lists are mutable we can change them.
print(h[2])
h[2] = 300
print(h[2])

#doing tree indexing to get "tyu" and change it to "jak"
print(h)
h[10][1]
h[10][1] = "jak"
print(h[10][1])

#we can use del command and idexing to delete specific element in the list
print(h[3])
del(h[3])
print(h[3])

#Create a list a_list, with the following elements 1, hello, [1,2,3] and True
a_list = [1, "hello", [1,2,3],True]

#Find the value stored at index 1 of a_list
a_list[1]

#Retrieve the elements stored at index 1, 2 and 3 of a_list.
a_list[1:4]

#Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:
A = [1, 'a']
B = [2, 1, 'd']
A+B

############################SETS#################################

#They are also a type of collection
#This means that like lists and tuples,you can input different Python types.Unlike lists and tuples, they are unordered.
#You place the elements of a set within the curly brackets{}.

set1 = {"jak","rock",4,5,7,7,2.2,100.23,"rock"}
print(set1)

#in the result duplicate elements on sets are removed automatically 


#You can convert a list to a set by using the function set,this is called type casting.

list1 = ["hi","rock",33,45.67,0.0094,"tyu",99.00]
print(type(list1))
newset = set(list1)
print(newset)
print(type(newset))


#using add method on sets
seta = {2,3,4,5,6,6,"hi","world"}
seta.add("new value")
print(seta)

#using remove method on sets
seta.remove(4)
print(seta)

#We can verify if an element is "in" the set using the in command
print("world" in seta)
print("tuff" in seta)

# like in our old school venn diagram we can do intersection and union on sets
#intersection represented in python as "&"

set1 = {"mike","fire","ice",4,5,12,8}
set2 = {"hi","mike","ice",8}

set3 = set1 & set2
set4 = set1.union(set2)

print(set3)
print(set4)

###########################Dictionaries################################
#A dictionary has keys and values
#key is analogous to the index, they are like addresses but they don’t have to be integers. They are usually characters
#To create a dictionary, we use curly brackets
#The keys are the first elements; they must be immutable and unique. 
#Each key is followed by a value separated by a colon. The values can be immutable, mutable and duplicates

dictionary = {"key1" : 1,"key2" : 5,"key3" : ("hi world","jkjkj",4,5),"key4":[7,5,10]}
print(type(dictionary))

app = {"name": "vissu", "age": 29, "cell":4383377678}
#in this name,age,cell are keys and vissu,29,4383377678 are values for the keys
#we can call values by using keys

print(app["name"])
print(app["age"])
print(app["cell"])

#adding new value to the dictionary
app["address"] ="unknow"
app["sex"]="male"

print(app)

#we can delete specific value in the dictionary by using del function and key

del(app["sex"])
print(app)

#To get all the keys in the dictionaries
app.keys()

#To get all the values in the dictionaries
app.values()


