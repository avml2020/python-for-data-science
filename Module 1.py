#Module 1

#use jupyternotebook for practice 
#use shift+enter to run each cell
#use # before the code to comment out or to explpain about the code in general
#use control and # to comment multiple lines at the same time

#Print statement
#statement between paranthasis is called as argument
print("simple python")

# \n is used to print a seperate line 
print("hello \nworld")

print("Hi this is lesson 1 \n a simple print statement")

#--------------------------Data types--------------------------#
#Why we need to store data into different data types in python
#In Python, like in all programming languages, data types are used to classify one particular type of data. 
# This is important because the specific data type you use will determine what values you can assign to it and 
# what you can do to it (including what operations you can perform on it).for an example INT,FLOAT,STR

################################variables#####################################
#We use variables to store values
#It's good practice to use meaningful variable names, so you don't have to keep track of
# a simple example, we storing value 2.3 to variable a
a = 2.3
print(a)
# storing "simple pyton programing" to variable k\
k = "simple pyton programing"
print(k)

# We can assign a new value to old variable using the assignment operator.

original_h = 4
print(original_h)
changed_h = 6
print(changed_h)
using_h_toaddmore= h+5+5-45
print(using_h_toaddmore)


#example: Let’s say we would like to convert the number of minutes in the highlighted examples to number of hours

total_min = 43+42+57
print(total_min)
total_hr = total_min/60
print(total_hr)

###############################################################################
#use type function
print(type(4))
print(type(3.3))
print(type(0.444444))
print(type("simple python"))
print(type("TRUE"))

# we can change data types in python. This is called type casting
# NOTE: we can not change string like "kdkdkdk" to int and while we convert float to int we will loose the decimal places 
#21 is int but by adding float it can be changed to float

a = 21
print(type(a))
a = float(a)
print(type(a))

#"1" is considered as string, but by casting it with int it is converted into int

b = "1"
print(type(b))
b = int(b)
print(type(b))

#2.3 is float and converted into int and we in int conversion we loose .3 

c= 2.3
print(type(c))
c = int(c)
print(c)
print(type(c))

# converting int to bool
d = 1
print(d)
d = bool(d)
print(d)
print(type(d))

#mathamatical operations 
# 34+10-4*3/1  in ths expression We call the numbers operands and the maths symbols are called operators

print(2*3)
print(5+4)
print(6-9)
#we can use / for division and the result is float value
print(37/4)
#we can use // for division and the result is int value and rounded
print(37//4)

######################################################strings#######################################
#strings : A string is contained within two quotes
#It is helpful to think of a string as an ordered sequence
#Each element in the sequence can be accessed
#using an index represented by the array of numbers.
a_string = "Hi this is a simple python course for data science course"
#get string Hi
print(a_string[0:2])
#lasr char in the string
print(a_string[-1])

#We can concatenate or combine strings. We use the addition symbols.

a = "first"
b = "second"
c = "3"

final = a+b+c
print(final)

#We can replicate values of a string. We simply multiply the string by the number

final_3times = final*3
print(final_3times)

#applying methods to strings
#When we apply a method to the string "A”,we get a new string “B" that is different from "A".
#using upper method

a = "hi world hi people"
b = a.upper()
print(b)

#using replace method

a = "hi world"
b = a.replace("world","everyone")
print(b)

#using find method
name = "Michael jackson"
name.find("l")
name.find("jac") # it will give you the index position of j





