'''
# the simplist version, the reusability is bad,
# because there is no returning value in fab(max)
def fabs(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1


# the version, using a list to save the numbers. However,
# the memory required to store the numbers is increasing with bigger max.
# to control memory usable, its better to use iterable object to replace list.
def fab2(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L


print(fab2(5))
for n in fab2(5):
    print(n)


# the iterable version with class ,
# but it is not so concise as the first version

class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


for n in Fab(5):
    print(n)

#using yield to achieve reusability, memory-efficiency, and concision.
def fab(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
for n in fab(5):
    print(n)
'''


def is_palindrome(n):
    '''
    mystring=''
    for i in range(0,len(str(n))):
        mystring=mystring+str(n)[-1-i]
    if str(n)==mystring:


    if str(n) == str(n)[::-1]:
        return n
    '''
    return str(n) == str(n)[::-1]


print(list(filter(is_palindrome, range(1, 1000))))
