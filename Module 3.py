#Module 3

#conditions and branching

#Comparison operations compare some value or operand, then, based on some condition they produce a boolean

a = 5
b = 10
# == is used to compare same or not
print(a==b)

name1= 'vissu'
name2='anantha'
print(name1==name2)

id1 = 10
id2 = 10.0
print(id1==id2)

#using >,<,!=(not equal)

a = 10
b = 25

print(a>b)
print(b>a)
print(a!=b)

#Branching allows us to run different statements for a different input(if conditions)
#if the given customer age is greater than 18 he can join the club, if not say not qualified
age_condition = 18
cutomer_age = 17


if (cutomer_age>=age_condition):
    print("you can join the club")
print("not qualified")

#using if else condition
##if the given customer age is greater than 18 he can join the club,else say join teens club,and finally say  say move on

if (cutomer_age>=age_condition):
    print("you can join the club")
else:
    print("join teens club")
print("move on")

#The elif statement, short for else/if, allows us to check additional conditions if the preceding condition is false. 
#If the condition is true, the alternate expressions will be run
#say if age is > 17 "join the club", age = 17 join teen sports club, else say join teen club ,and finally say  say move on

if (cutomer_age>age_condition):
    print("you can join the club")
elif(cutomer_age==17):
    print("join teen sports club")
else:
    print("join teen club")

print("move on")

##################logical operators #######################################

#for or condition
#a=true b=true  finalresult=true
#a=true b=false finalresult=true
#a=false b=false finalresult=false

#for and condition
#a=true b=true  finalresult=true
#a=true b=false finalresult=false
#a=false b=false finalresult=false


#############################################################################
#using (and) operator
#for an example a stuent can only get admission if his age is 20 and test marks are 90. In this case we use and condition

age_condition = 20
testmarks_condition = 90

#case1 : student1 age is 20 and marks are 95
student1_age = 20
student1_marks = 95

if (student1_age>=age_condition and student1_marks >= testmarks_condition):
    print("congratulations you got admission")
else:
    print("try next time")

#case1 : student2 age is 19 and marks are 88
student2_age = 19
student2_marks = 88

if (student2_age>=age_condition and student2_marks >= testmarks_condition):
    print("congratulations you got admission")
else:
    print("try next time")
    
##using (or) operator
#for an example a stuent can only get admission if any of the condition is satisfied. eaither age is 20 or test marks are 90. 
#In this case we use or condition

age_condition = 20
testmarks_condition = 90

#case1 : student1 age is 20 and marks are 95
student1_age = 20
student1_marks = 95

if (student1_age>=age_condition or student1_marks >= testmarks_condition):
    print("congratulations you got admission")
else:
    print("try next time")

#case1 : student2 age is 19 and marks are 88
student2_age = 19
student2_marks = 55

if (student2_age>=age_condition or student2_marks >= testmarks_condition):
    print("congratulations you got admission")
else:
    print("try next time")
    

##################################LOOPS############################################
#range function
#range(N) means it will consider from 0 to N-1
#range(5) means (0,1,2,3,4)
#range(10,14) menas (10,11,12,13)

#Loops perform a task over and over.

#examplpe1 : consider one list having names and i want to replace all the names with jak 

names_list = ["raj",'mike','dan','hak']
print(names_list)

#style 1 using range function

for i in range(0,4):
    names_list[i] = 'jak'
print(names_list)

#style 2 : by using in we taking all the elemets into given name k and printing one afer one

names_list2 = ["raj",'mike','dan','hak']
print(names_list2)

for k in names_list2:
    print(k)
    
#style 3 : we can use enumerate to see which neme is under which index
#in below example i am using count to store index count coming from enumerate and i is the place holder one by one from the names_list2
# for more details about enumerate : https://www.geeksforgeeks.org/enumerate-in-python/

for count,i in enumerate(names_list2):
    print(count,i)


############################“While loops”###################### 
#similar to “for loops”, but instead of executing a statement a set number of times, a while loop will only run if a condition is met.

# example : we have a list with 6 elements. 5 elements are orange and one element is blue. 
# i have to check each and every element and insert into a new list 
#I have to check one by one and have to stop when i see the blue element

colors = ["orange", "orange", "orange","blue", "orange", "orange"]
new_colors = []
i=0

while(colors[i]=="orange"):
    new_colors.append(colors[i])
    i = i+1
    
print(new_colors)

#more examples:
#Write a for loop the prints out all the element between -5 and 5 using the range function.
for i in range(-5,5):
    print(i)

#Print the elements of the following list using forloops: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] 

Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for names in Genres:
    print(names)
    
#Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. 
#If the score is less than 6, exit the loop.  
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0

while (PlayListRatings[i] >= 6):
    print(PlayListRatings[i])
    i = i+1
	
#functions: The function is just a piece of code you can reuse
#Python has many built-in functions; you don't have to know how those functions work internally,but simply what task those functions perform
#methods are similar to functions
#using lenght(len) function
l = [6,5,1,89,0.0]
print(len(l))

#using inbuilt sum finction
l1 = [10,5]
print(sum(l))

#using sorted function
l2 = [5,6.7,2,1,55,65]
print(sorted(l2))

#writing our own function add
#take a input and add 1 to the input and return the result

def add(a):
    b = a+1
    return b
#calling function
print(add(5))

#writing our own function take
#a function can do multiple actions 

def take(a,b):
    c = a*3
    d = b*3
    e = c+d;
    print("given value for a is ",a);
    print("given value for a is ",b);
    return e

#calling take function
print(take(4,2))

#we can use loops in the functions;
#creating a fucntion to take list as input and writing loop inside to display index and value from the list

def display(a):
    for i,k in enumerate(a):
        print("index ",i,"in the list is ",k);

#calling finction for the list l
l=["raj","jak","mike"]
display(l)


#global variable : A global variable can be reached anywhere in the code.
#local variable  : a local variable can be reached only in the scope.

#a variable inside the function is called as local variable
def mul(a):
    #declaring local variable
    var_b = 10
    return var_b*a;

#calling function
print(mul(9))
#trying to call local variable var_b : u will get an error"name 'var_b' is not defined"
#uncoment below statement and try
#print(var_b)

#declaring global variable and using where ever we need
#global variable

var_a = 2

def minus(c):
    #using global variable inside
    d = var_a
    return c-d;

#calling function

print(minus(10))

#########################################objects and classes#########################################
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

#example for objects
a = 20
b = "string"
c = (1,3,4,5,"new")
d = ["rules",2,"break"]
#all the above are objects
#now we will create a class on top of the object to hold the the objects. 
#in other words we can call class as a adress for the objects.
#1
class intclass(object):
    a=20
#calling a in the class "intclass"
print(intclass.a)

#2
class strclass(object):
    b = "string"
#calling a in the class "strclass"
print(strclass.b)

#3
class tupleclass(object):
    c = (1,3,4,5,"new")
#calling a in the class "tupleclass"
print(tupleclass.c)

#4
class listclass(object):
    d = ["rules",2,"break"]
#calling a in the class "listclass"
print(listclass.d)

#the __init__() function
#it is a built in function used in every class
#it will executed when the class is called
#it is used to assign values to object properties
#example

class circle(object):
    def __init__ (self,radius,color):
        self.radius = radius;
        self.color = color;
#calling cirle class with given radius and color
#1
c1 = circle(10,"red")
print(c1.radius)
print(c1.color)

#2
c2 = circle(200,"white")
print(c2.radius)
print(c2.color)

#adding methods under the calss 

class circle_obj(object):
    #here i am giving some default values as constant atributes to the class
    def __init__(self,radius=10,color="red"):
        self.radius = radius
        self.color = color
    #creating method 
    def add_radius(self,r):
        self.radius = self.radius+r
#assign class circle_obj to a atribute
c2=circle_obj()
#calling radius 
print(c2.radius)
#calling color
print(c2.color)
#calling method created add_radius and giving parameter value for the method
c2.add_radius(10)
#now calling radius variable to see how the canges are done
print(c2.radius)





    



    