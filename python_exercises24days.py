'''# 1st day
# 1.1: Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        print (i,end=',')
print('\n')

print(*(i for i in range(2000,3201) if i%7==0 and i%5!=0),sep=',')

# 1.2:Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input: 8 Then, the output should be:40320

n = int(input('Enter a number please:'))
#Solution 1
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)

#Solution 2
def shortFact(x): return 1 if x <= 1 else x * shortFact(x - 1)
print(shortFact(n))

#Solution 3
from functools import reduce


def fun(acc, item):
    return acc * item


print(reduce(fun, range(1, n + 1), 1))
#Solution 4: recursion
def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)
print(fact(n))

# 1.3: With a given integral number n, write a program to generate a dictionary
# that contains (i, i x i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.Suppose the following input: 8
# Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.
try:
    n = int(input("Please enter a number: "))
except ValueError as err:
    print(err)


# Solution 1
def func(n):
    d = {}
    # d=dict()
    for i in range(1, n + 1):
        d[i] = i * i
    print(d)


func(n)

# Solution 2
d = {i: i * i for i in range(1, n + 1)}
print(d)

# Solution 3
print(dict(enumerate([i*i for i in range(1,n+1)], 1)))
'''
# 2nd day
