# Question 1
# Write a function to print "hello_USERNAME" "USERNAME" is the input of the function.
#  The first line of the code has been defined as below.

def hello_name(user_name):
    print(f"Hello_{user_name}!")

hello_name("USERNAME")

# Question 2
# Write a function first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
   x= range(100)
   for n in x:
    if n%2 != 0:
        print(n)

first_odds()

# Question 3
# Please write a Python function,
# max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    a_list.sort()
    greatest_num = a_list.pop()
    print(greatest_num)
  
max_num_in_list([1,2,4,3,5,6,4,11,22,33,55,44665,32,54,3,33])

# Question 4
# Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100, 
# unless it is also divisible by 400. The return should be boolean type

def is_leap_year(a_year):
    if a_year%4 == 0 and a_year%100 !=0 and a_year%400!=0:
        return True
    else:
        return False

print(is_leap_year(1807))
print(is_leap_year(1808))
# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2, 3, 4, 5, 6]

def is_consecutive(a_list):
    is_consecutive = all(a_list[i] == a_list[i-1] + 1 for i in range(1, len(a_list)))

    print(is_consecutive)

is_consecutive([1,2,3,4,5,6])
is_consecutive([1,1,2,3,4,5,6])


