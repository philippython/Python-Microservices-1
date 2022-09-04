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
past = list(filter(lambda word , char:  char in word, ["laughed", "pray", "killed", "raped", "race"]))
print(past)

# reducing
multi = reduce(multipy, transactions, 1)
print(multi)