"""
#page -> http://www.w3resource.com/python-exercises/string/#EDITOR
# 1 exercise
print(len('school'))
# 2 exercise

import collections
print(collections.Counter("Google.com"))

#3 exercise
list = [1, 3, 5]
print max(list)
#4 exercise
sample_list = [8, 2, 3, 0, 7]
print sum(sample_list)
#5
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print multiply((8, 2, 3, -1, 7))
#6
string = "1234abcd"
print string[::-1]
#7
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))
#8
temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", o_convention, "is", result, "degrees.")
#9
#Create an empty tuple
x = ()
print(x)
# Create an empty tuple with tuple() function built-in Python
tuplex = tuple()
print(tuplex)"""
#10
import time
import datetime
print("1: Current date and time: ", datetime.datetime.now())
print("2: Current year: ", datetime.date.today().strftime("%Y"))
print("3: Month of year: ", datetime.date.today().strftime("%B"))
print("4: Week number of the year: ", datetime.date.today().strftime("%W"))
print("5: Weekday of the week: ", datetime.date.today().strftime("%w"))
print("6: Day of year: ", datetime.date.today().strftime("%j"))
print("7: Day of the month : ", datetime.date.today().strftime("%d"))
print("8: Day of week: ", datetime.date.today().strftime("%A"))
#11
import time
x = time.localtime(time.time())
print "Current Year:", x[0]
print "Current Month", x[1]
print "Current Day", x[2]
print "current Hour", x[3]
print "current Minute", x[4]
print "current second", x[5]
print "current day of week", x[6]
print "day in the year", x[7]
print "current day light saving", x[8]

#12
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))