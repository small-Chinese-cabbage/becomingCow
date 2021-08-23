import math
def binary_search(list,item):
    low=0
    high=len(list)-1

    while low<=high:
        mid=math.ceil((low+high)/2)
        guess=list[mid]
        if guess==item:
            return mid
        elif guess<item:
            low=mid+1
        else:
            high=mid-1

my_list=[1,3,5,8,9]
print(binary_search(my_list,10))