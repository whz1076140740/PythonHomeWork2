# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

def car_at_light(light):
    try:
        if light.__eq__("red"):
            return "stop"
        elif light.__eq__("green"):
            return "go"
        elif light.__eq__("yellow"):
            return "wait"
        else:
            raise Exception("Undefined Color")    
    except Exception as err:
        print(err,"\n")
    return 

print(car_at_light("red"))
car_at_light("nocolor")
# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 
def safe_subtract(a,b):
    try:
        result = a - b
        return result
    except TypeError as err:
        print(err)
        result = None
        return result

testStr = "test"
a = 5
b = 6

print(a, " - ", b, " = ", safe_subtract(a,b))
result = safe_subtract(testStr,b)
print(testStr, " - ", b, " = ", "None" if result == None else result )

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lby


# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#

def read_data(fileName):
    try:
        with open(fileName) as file:
            line = file.read()
        print(line)
    except FileNotFoundError:
        print("File:", fileName," Not Exists")
        choose = input("Do you want to create? Input Y or N")
        if choose == "Y":
            print("Creat File Not Implement")
    except Exception as err:
        print(err)

read_data("data.csv")


# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += elem

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = string+"_"+string

### (c) Careful!
j=10
while j > 0:
   j += 1

### (d)
productory = 0
for elem in [1, 5, 25]:
    productory *= elem


