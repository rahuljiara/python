# 

# 



# OUTPUT In Python
print("Hii Bro")
print("Myself Rahul Ji Ara")
print("You are welcome to the", "My World")
print(1)


# Variables In Python   -  variableName = Value
print()
print("VARIABLES")
name = "Rahul Ji Ara"
age = 23
edu = "B.tech"
print("I am", name)
print("My age is", age)
print("My Qualification is", edu)

print()
print("Data Type of name variable is ", type(name))
print("Data Type of age variable is ", type(age))
print("Data Type of edu variable is ", type(edu))

print()
print("Data Types")
a = 1
b = 2.34
c = -2.3
d = True
e = False
f = None
print("Data Type Of a :", type(a))
print("Data Type Of b :", type(b))
print("Data Type Of c :", type(c))
print("Data Type Of d :", type(d))
print("Data Type Of e :", type(e))
print("Data Type Of f :", type(f))
print()
str1 = "String"
str2 = 'String'
str3 = """String"""
print("Data Type Of str1", type(str1))
print("Data Type Of str2", type(str2))
print("Data Type Of str3", type(str3))

# OPERATORS
print("Arithmatic Operators")
print(2+3)  # Addition
print(12-4) # Substraction
print(4*3)  # Multiplication
print(16/4) # Division
print(16%5) # Reminder
print(2**3) # Power 2^3

print()
print("Comparison Operator")
x = 20
y = 45.4

print(x==y)
print(x!=y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)

# Type Conversion
print()
sum = x+y #automatically converted into superior data types - int -> float 
print(sum)

x = float("20") # string converted into float
print(x)

y = int("20") # string converted into iteger
print(y)
y = int(20.44) # integer converted into float
print(y)
y = (20.44) # integer converted into float
print(y)

# Input In Python
print()
stdName = input("Enter Your Name\t: ")
stdAge = int(input("Enter Your Age\t: ")) #Only integer value is allowed 
stdDept = input("Enter Your Department\t: ")
stdId = stdName + stdDept + str(stdAge)
print("Student Id \t", stdId, "\nLength of Id is \t:",len(stdId))
print(stdName," Is", stdAge," years Old & Student of", stdDept, " Department")