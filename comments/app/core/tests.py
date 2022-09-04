# from django.test import TestCase
from functools import reduce
# Create your tests here.

def multipy(*args):
    sum = 1
    for num in args:
        sum *= num
    return sum

print(multipy(6, 7, 8, 8))

# mapping with one parameter
transactions = [1200, 890, 456, 787, 5675]
charge = lambda credit : credit - 500
net_transactions = list(map(charge, transactions))

print(net_transactions)

#  mapping with two parameters
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 7)))
print(result)

# filtering 
past = list(filter(lambda word :  'd' in word, ["laughed", "pray", "killed", "raped", "race"]))
print(past)

# reducing
multi = reduce(multipy, transactions, 1)
print(multi)

#exercise

fruits = set(('apple', 'banana', 'groundnut', 'maize'))
print(fruits)

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than 
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: round(x, 3), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 + num2, my_numbers, 0)

print(map_result)
print(filter_result)
print(reduce_result)


def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)