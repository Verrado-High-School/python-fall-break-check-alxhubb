# This is a check/review to make sure nothing was "lost" over break


# Alex Hubbard
# Period 1

# Variable delaration and assignment
# Example
myVar = "hello"
# You try, delcare two variables 1 string and 1 number, assign values
number = 1
string = "yeet"

# while loop
# example
x = 10
while x > 0:
	print(x)
	x = x - 1



# you try, print your name 100 times

name = input("What is your name?")
while x < 100:
	print(name)
	x = x + 1

# Don't do this
#   print("Alex" * 100)


# string concatenation
# exampple
name = "Alex"
print("Hello " + name)
# make a variable with your favorite movie
# print "my favorite movie is"
favMovie = "The Hitman's Bodyguard"
print("My favorite movie is " + favMovie)

# input 
# example 
myName = input("What is your name: ")
print("Your name is: " + myName)

# promt for favorite song and print "Your favorite song is"
song = input("What is your favorite song?")
# casting: changing the type of variable
Num = 40
print("My number is " + str(Num))
num1 = input("enter a number: ")
num1 = int(num1) + 10
print("num1 + 10 is " + str(num1))

# ask for two numbers, add thyem and print the answer
var1 = input("Give me a number: ")
var2 = input("give me another number: ")
var3 = int(var1) + int(var2)
print("Your number is " + str(var3))

# if/else
# example
number = int(input(" Type a number "))

if number > 100:
	print("Your number is more than 100")
elif number == 100:
	print("Your number is equal to 100")
else:
	print("your number is less than 100")


# ask if today is your birthday, if it is print happy birthday
bday = input("Is today your birthday?")
if bday == "yes":
	print("Happy Birthday!!")
else:
	print("have a good day")