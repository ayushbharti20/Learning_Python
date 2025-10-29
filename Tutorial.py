''' 

# Strings
word = "Leonardo"

# string concatination 
word = word + " da Vinci"
print(word) 

#Indexing 
print(word[0])
print(word[5])
print(word[-1])

# Slicing
print(word[0:10])
print(word[10:15])
print(word[:11])
print(word[5:])
print(word[-6:])
print(word[:9]+word[9:])

#length of string
print(len(word))

#string Functions
print(word.capitalize())
print(word.casefold())
print(word.lower())
print(word.center(25))
print(word.center(25,'*'))
print(word.center(10)) # if the width is less than the string length, it returns the original string
print(word.count('a')) 

# count to find subtring fron a specific index to a specific index
print(word.count('a',5,15))
print("abbracadabra".count('a',5,12))

print("My name is {}".format(word))
print(word.endswith("Vinci"))
print(word.startswith("Leo"))


# alphanumeric check
print(word.isalnum())
print("abc123".isalnum())
print("a".isalpha())
print("abc".isalpha())
print("abc123".isalpha())
print(" ".isspace())    
print("123".isdecimal())
print("123".isdigit())
print("123".isnumeric())
print("String".islower())
print("string".islower())
print("STRING".isupper())   
print("String".istitle())
print("This Is A Title".istitle())
print("   python   \'".lstrip())
print("   python   ".rstrip())
print("Arthur: Three".removeprefix("Arthur: "))
print("Arthur: Three".removesuffix(" Three"))
print("This is String".partition(" "))
print("This is a String".replace("is","at"))
print("This is a String".replace("is","at",1)) # only first occurance
print("1,2,3,4,5".split(","))
print("this is a string".split(" "))
print("this-is-a-string".split("-",1)) # only first occurance

print(word.swapcase())


# f-strings (formatted string literals)
name = "Leonardo da vinci"
age = 67
print(f"My name is {name}. I am {age} years old.")

num = 3.14159
print(f"Value of pi is approximately {num:.2f}.")  # rounds to 2 decimal places

# printf style string formatting
name = "Leonardo da Vinci"
age = 67
print("My name is %s. I am %d years old." %(name,age))
num = 3.14159
print("Value of pi is approximately %.2f." %num)  # rounds to 2 decimal places

'''

'''
#cantrol flow statements

x = 20
if x <= 0 :
    print("x is a negative number or zero") 
elif x > 0 and x <18:
    print("x is minor")
else:
    print("x is an adult")
'''

'''
#loops 
# for loop

list1 = ["Robot","AI","Machine Learning","Data Science"]
for items in list1: # to iterate through each item in the list
    print(items)

for  i in range(11): # to iterate through a sequence of numbers from 0 to 10
    print(i)

for i in range(1,11,2): # to iterate through a sequence of numbers from 0 to 10 with a step of 2
    print(i)

dict1 = {1:"Robot",2:"AI",3:"Machine Learning",4:"Data Science"}

for key in dict1: # to iterate through the keys of the dictionary
    print(key,dict1[key])

for key,value in dict1.items(): # to iterate through the keys and values of the dictionary
    print(key,value)

for value in dict1.values(): # to iterate through the values of the dictionary
    print(value)

'''


'''
#while loop

count = 0
while count < 5:
    print("Count is:",count)
    count += 1  

# break and continue statements
for i in range(10):
    if i == 5:
        break # exit the loop when i is 5
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue # skip the even numbers
    print(i)

# pass statement
for i in range(5):
    if i == 3:
        pass # do nothing when i is 3
    else:
        print(i)

'''

'''
# match statement

day = input("Enter a day of the week: ")
match day:
    case "Monday":
        print("Its Monnday")
    case "Tuesday":
        print("Its Tuesday")
    case "Wednesday":
        print("Its Wednesday")
    case "Thursday":
        print("Its Thursday")
    case "Friday":
        print("Its Friday")
    case "Saturday":
        print("Its Saturday")
    case "Sunday":
        print("Its Sunday")
    case _: # default case
        print("Invalid day")

'''

'''
# functions

num = int(input("Enter a number: "))
def fib(n):
    a , b = 0 , 1
    while a < n:
        print(a,end=" ")
        a,b = b , a+b
    print() 
fib(num)


#order of arguments passing in function : 
#1. positional arguments :- positional arguments are used to pass arguments to a function based on their position
#2. *arguments :- *arguments are used to pass a variable number of non-keyword arguments to a function in the form of a tuple
#3. default arguments :- default arguments are used to provide default values for function parameters if no value is passed
#4. **arguments :- **arguments are used to pass a variable number of keyword arguments to a function in the form of a dictionary


def all_arg(a, / ,b,*, c):
    print("This i positional arguments:",a)
    print("This can be position or keyword argument:",b)
    print("This is keyword argument:",c)

all_arg("pos" , b="pos_or_key" , c = "keyword")
all_arg("pos" , "pos_or_key" , c = "keyword")

# lamda expression
square = lambda x:x*x
print(square(5))

'''
# documentation string

#def my_function():
#    '''This is a docstring. This function does nothing. '''
#    pass 
#print(my_function.__doc__)

# Data Structures

'''
# Lists
my_list = [1,2,3,4,5]
print(my_list)

#indexing and slicing
print(my_list[0])
print(my_list[-1])
print(my_list[1:4])
print(my_list[::2])
print(my_list[::-1])# reverse the list

#concatination
my_list = my_list + [6,7,8,9,10]
print(my_list)

print(len(my_list))

my_list.append(11)# append 11 at the end of the list
print(my_list)
my_list.append(2*6)
print(my_list)

my_list[5:]=[]
print(my_list)

my_list.extend([6,7,8,9,10])
print(my_list)

my_list.insert(0,0)# insert 0 at index 0 and shift the rest of the elements to the right
print(my_list)

my_list.remove(0) # remove the first occurrence of 0
print(my_list)

my_list.pop() # remove the last element
print(my_list)
my_list.pop(0) # remove the element at index 0
print(my_list)

print(my_list.index(5)) # return the index of the first occurrence of 5
my_list.append(1)
my_list.append(5)
print(my_list)

print(my_list.count(5)) # return the number of occurrences of 5

my_list.sort()# sort the list in ascending order
print(my_list)
my_list.sort(key= lambda x: x*x,reverse = True) # sort the list based on the square of the elements in descending order
print(my_list)

my_list.reverse() # reverse the list
print(my_list)

print(my_list.copy()) # return a copy of the list

my_list.clear() # remove all elements from the list
print(my_list)

'''

'''
#List as stack
stack = [1,2,3,4]
stack.append(5)
stack.append(6)
print(stack)

stack.pop()
stack.pop()
print(stack)

'''

'''
# list as queue using deque from collections module
#FIFO - First in first out

from collections import deque
queue = deque([1,2,3,4])# create a deque object
queue.append(5) # add 5 to the right end of the deque
queue.append(6) # add 6 to the right end of the deque
print(queue)

queue.popleft() # remove and return the leftmost element
print(queue)

'''
'''
# List Comprehensions

squares1 = list(map(lambda x: x*x , range(10))) # using map and lambda function
print(squares1)
square2 =[x*x for x in range(10)] # using list comprehension
print(square2)

even_squares = [x*x for x in range(10) if x%2 == 0] # using list comprehension with condition
print(even_squares)

list1 = [(x,y) for x in [1,2,3] for y in [5,3,1] if x!=y] # using list comprehension with multiple for loops and condition
print(list1)

num = int(input("Enter a number: "))
even_list = [x for x in range(num+1) if x%2==0]
odd_list = [x for x in range(num+1) if x%2!=0]
print("Even numbers:",even_list)
print("Odd numbers:",odd_list)

'''

'''
# Nested list comprehensions
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
transposed = [[row[i] for row in matrix] for i in range(3)] # transpose the matrix
print(transposed)

'''

'''
# The Del Statement
my_list = [1,2,3,4,5]
print(my_list)
del my_list[0] # delete the first element
print(my_list)
del my_list[1:3] # delete elements from index 1 to 2
print(my_list)
del my_list[:] # delete all elements
print(my_list)

'''

'''
# Tuples and Sequences
tuple1 = (1,2,3,4,5) 
empty_tuple = () # empty tuple
singleton_tuple = (1,) # tuple with one element
print(len(tuple1))
print(len(empty_tuple))
print(len(singleton_tuple))
tuple2 = 1,"one",2.0,"two" # tuple without paranthesis and mixed data types
print(tuple2)
#tuple1[2] = 10 # tuples are immutable will throw error

print(tuple1[0])
print(tuple1[1:4])
print(tuple1[::-1])
print(tuple1 + (6,7,8)) # concatination
print(tuple1 * 2) # repetition
print(3 in tuple1) # membership test
print(10 in tuple1) # membership test

'''

'''
# Sets 
 
empty_set = set() # empty set
set1 = {1,10,20,5,6} # set with elements
set2 = {10,5,8,9,20} # another set with elements
print(set1)
print(len(empty_set))
print(len(set1))
print(set1  | set2) # union (all elements)
print(set1 & set2) # intersection (common elements)
print(set1 - set2) # difference (elements in set1 but not in set2)
print(set1 ^ set2) # symmetric difference  (elements in either set1 or set2 but not in both)
set3 = {1,2,3,4,4,5,5,6}  # set with duplicate elements
print(set3) # duplicate elements are removed
print(len(set3))

#set comprehensions
squares = {x*x for x in range(10)}
print(squares)

# set methods
set1.add(15) # add 15 to set1
print(set1)
set1.remove(15) # remove 15 from set1, will throw error if
print(set1)
set1.discard(10) # remove 10 from set1, will not throw error if 10 is not present
print(set1)
set1.pop() # remove and return an arbitrary element from set1
print(set1)

'''

'''
# Dictionaries

    # key:value pairs
    # key contain only immutable data types , unique and unchangeable
    # values can contain any data type

dict1 = {'name':"Leonardo da Vinci",'age':67,'profession':"Artist"}
print(dict1)
dict1["famous_work"] = "Mona Lisa" # add a new key-value pair
print(dict1)
del dict1["age"] # delete a key-value pair
print(dict1)
print(dict1.keys()) # return the keys of the dictionary
print(dict1.values()) # return the values of the dictionary
print(dict1.items()) # return the key-value pairs of the dictionary
dict_list = list(dict1) # convert the dictionary to a list of keys
print(dict_list)
dict_list1 = list(dict1.items()) # convert the dictionary to a list of key-value pairs
print(dict_list1)
sorted_dict = dict(sorted(dict1.items())) # sort the dictionary by keys
print(sorted_dict)

dict2 = dict(name="Albert Einstein",age = 76 , profession = "Physicist") # another way to create a dictionary
print(dict2)

# Dictionary comprehensions
squares = {x:x*x for x in range(1,5)} # create a dictionary with keys as numbers and values as their squares
print(squares)

'''

''' 
# Module and Packages
import fibonacci # import the fibonnaci file from the current directory as a module
print(fibonacci.fibonacci(10))


# onother method but not recommended as it can lead to naming conflicts(your function with same name will get replaced)
from fibonacci import fibonacci # import only the fibonacci function from the fibonacci module
print(fibonacci(15))


# import with alias 
import fibonacci as fib # import the fibonacci module with an alias
print(fib.fibonacci(20))

'''

'''
# Packages
from math_tools import * # import all functions from the math_tools package

print(add(10,5))
print(subtract(10,5))
print(multiply(10,5))
print(divide(10,5))
print(sin_deg(30))
print(cos_deg(60))
print(tan_deg(45))

'''

'''
# String Templates
from string import Template
s = Template("Hallo ist bin $name. Ich bin sehr klug") # German -> Eglish : Hello i am "name", I am very smart
sentence = s.substitute(name="Leonardo da Vinci")
print(sentence)

s2 = Template("Der Hund ist Name: $hund_name und die katze Name: $Katze_name")
sentence2 = s2.safe_substitute(hund_name = "Cooper")
print(sentence2) # will not throw error for missing Katze_name and will leave it as is
sentence3 = s2.safe_substitute(hund_name = "Cooper",Katze_name="Luna")
print(sentence3)

'''
'''
# Reading and Writing Files

# r = readmode , w = writemode , a = appendmode(opens the file for appending , any data writen in the file will be automatically added to the end) , r+ = read and write mode , b = binary mode(Binary mode data is read and written as bytes objects. You can not specify encoding when opening file in binary mode.)
with open("file.txt","r") as file: # open the file in read mode
    content = file.read() # read the entire content of the file
    print(content)
    print(file.readline()) # read a single line from the file
    print(file.readline())
    #file.close() is not required as with statement automatically closes the file

with open("file.txt","r") as file:
    for line in file: # read the file line by line
        print(line,end='') 



with open("file.txt","w") as file: # open the file in write mode
    print(file.write("This is a new line added to the file.\n")) 
    print(file.write("This is another line added to the file.\n"))
    # it will return the number of characters written to the file
    # it will also overwrite the existing content of the file
    print(file.tell()) # return the current position of the file pointer as an integer which is the number of characters from the beginning of the file
     


with open("file.txt","r+") as file: # open the file in read and write mode. r+ doen not overwrite the existing content of the file
    print("Previous: ",file.read())

    file.write("This is line one.\n")
    print("Current Position: ",file.tell())

    file.write("This is line two.\n")
    print("New Position: ",file.tell())
    
    file.seek(0)
    print("Current: ",file.read())

'''















