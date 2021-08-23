'''
# exercise 4.1
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


# exercise 4.2
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


# exercise 4.3
def max(list):
    if list == []:
        raise ValueError
    elif len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

# quick sort
def quick_sort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if i<=pivot]
        greater=[i for i in arr[1:] if i>pivot]
        return quick_sort(less)+[pivot]+quick_sort(greater)
print(quick_sort([12,32,1,3,4,2,9]))
'''
# merge sort
