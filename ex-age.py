import datetime
import sys

#prompt user for an input

year_of_birth=int(input("Enter your year of birth:"))

#current year

current_year= datetime.datetime.now().year

#computing the user age based on current year

age=current_year - year_of_birth

#display age

print("your age is:",age)

#prompt the user to enter height

height=float(input("Enter your height in meters:"))

#display the height

print(f"Your height is:{height:.2f}")

#determining the datatypes

print ("the datatype for year of birth is:",type(year_of_birth))
print ("the datatype for age is:",type(age))
print ("the datatype for height is:",type(height))

#Determining the size of each input and display it

print ("the size for year of birth is:",sys.getsizeof(year_of_birth))
print ("the size for age is:",sys.getsizeof(age))
print ("the size for height is:",sys.getsizeof(height))


