# from django.test import TestCase

# Create your tests here.

def multipy(*args):
    sum = 1
    for num in args:
        sum *= num
    return sum

print(multipy(6, 7, 8, 8))