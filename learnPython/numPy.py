import numpy as np

'''
#创建0到4维数组，打印数组以及他们的维度
arr0=np.array(1)
arr1=np.array([1,2,3,4])

arr2=np.array([[1,2,3,4],[4,5,6,7],[1,2,3,5]])
arr3=np.array([[[1,2,3,4],[4,5,6,7]],[[4,3,2,1],[7,6,5,4]]])
arr4=np.array([1,2,3,4],ndmin=4)

#print(arr0, "is a ",arr0.ndim,"d array")
#print(arr1, "is a ",arr1.ndim,"d array")
print(arr2, "is a ",arr2.ndim,"d array")
print(arr3, "is a ",arr3.ndim,"d array")
print("\n",arr3[-1,-1,-1])
#print(arr4, "is a ",arr4.ndim,"d array")


# 裁切一维数组

arr=np.array([0,1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[4:])
print(arr[:4])
print(arr[-3:-1])
print(arr[-7:-1:2])
print(arr[::2])


#裁切多维数组
arr2=np.array([[1,2,3,4],[4,3,2,1]])
print(arr2,"is a ",arr2.ndim,"dimension array")
print(arr2[0:2,0:3])

# 数组的数据类型
arrint = np.array([1, 2, 3, 4])
arrstring = np.array(['banana', 'grapefruit', 'lemon', 'mongo', 'strawberry'])

print(arrint.dtype)
print(arrstring.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

arr = np.array([1.1, 2.2, 3.3, 4.4])
newarr = arr.astype('i')
newarr2 = arr.astype(int)
newarr3 = arr.astype(bool)

print(arr)
print(newarr)
print(newarr.dtype)
print(newarr2)
print(newarr2.dtype)
print(newarr3)
print(newarr3.dtype)

#数组的副本和视图
#copy：互不影响
arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=61
x[1]=11

print(arr)
print(x)
print(arr.base, x.base)
#view：互相影响
arr=np.array([1,2,3,4,5])
x=arr.view()
arr[0]=61
x[1]=11

print(arr)
print(x)
print(arr.base, x.base)

#数组的shape:返回一个元祖依次表示从外维到内维元素的数量
arr=np.array([[[1,2,3,4],[4,3,2,1]],[[8,7,6,5],[5,6,7,8]]])
print(arr)
print(arr.shape)

arr=np.array([5,6,7,8],ndmin=5)
print(arr)
print(arr.shape)

# 数组重塑：改变数组的形状
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# 1d to 2d
newarr = arr.reshape(4, 3)
print(newarr, '\n')

# 1d to 3d
newarr1 = arr.reshape(2, 2, 3)
newarr2 = arr.reshape(2, 3, 2)
newarr3 = arr.reshape(1, 3, 4)
print(newarr1, '\n')
print(newarr2, '\n')
print(newarr3, '\n')

newarr4 = arr.reshape(1, 2, 2, 3)
print(newarr4,'\n')

print(newarr4.base)
print(arr)
#automatically calculating the last attribute for reshape
newarr5=arr.reshape(2,2,-1)
print(newarr5)
    #flattening the arrays
flattenedarray=newarr5.reshape(-1)
print(flattenedarray)

# iteration of the array
#1d
arr = np.array([1, 2, 3, 4])
for x in arr:
    print(x)
#2d
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 2, 4, 5]])
for x in arr:
    print(x)
for x in arr:
    for y in x:
        print(y)

#3d
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 2, 4, 5],[2,3,7,6]]])
for x in arr:
    print(x)
for x in arr:
    for y in x:
        print(y)
for x in arr:
    for y in x:
        for z in y:
            print(z)

# nditer(): can be used to replace the multi layer fors for high-dimensional arrays.
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 2, 4, 8], [8, 2, 3, 7]])

for x in np.nditer(arr):
    print(x, end=',')
print('\n')
for x in np.nditer(arr, order='F'):
    print(x, end=',')
print('\n')

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x, end=',')
print('\n')

print(arr)
print(arr.T)
print('\n')

for x in np.nditer(arr.T, order='C'):
    print(x, end=',')
print('\n')

for x in np.nditer(arr.T.copy()):
    print(x, end=',')
print('\n')

print(arr)
for x in np.nditer(arr[1:4, 1:4:2]):
    print(x, end=',')
print('\n')

#ndenumerate()
for idx,x in np.ndenumerate(arr):
    print(idx,x)

# Joining multiple arrays:

arrleft = np.array([[4, 3, 2, 1], [1, 2, 3, 4]])
arrright = np.array([[7, 6, 5, 4], [4, 5, 6, 7]])
# 1.concatenate按轴连接axis-based
arr = np.concatenate((arrleft, arrright))
arraxis1 = np.concatenate((arrleft, arrright), axis=1)
arraxis0 = np.concatenate((arrleft, arrright), axis=0)

print(arrleft)
print(arrright)
print(arr)
print(arraxis0)
print('\n')
print(arraxis1)
# 2.stack沿新轴连接stack-based
arr = np.stack((arrleft, arrright))  # default is axis =0
arraxis0 = np.stack((arrleft, arrright), axis=0)
arraxis1 = np.stack((arrleft, arrright), axis=1)

print("using stack for concatenating arrays")
print(arrleft)
print(arrright)
print('\n')
print(arraxis0)
print('\n')
print(arraxis1)
print('\n')

arrhstack = np.hstack((arrleft, arrright))#沿行堆叠
print(arrhstack)
print('\n')

arrvstack = np.vstack((arrleft, arrright))#沿列堆叠
print(arrvstack)
print('\n')

arrdstack = np.vstack((arrleft, arrright))#沿高/深度堆叠
print(arrdstack)
print('\n')

#splitting arrays
#1d
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,4)

print(newarr)
print(newarr[0])
for x in newarr:
    print(x)

# 2d
arr = np.array([[1, 2], [3, 4], [5, 6]])
newarr = np.array_split(arr, 3)
newarr1 = np.array_split(arr, 3, axis=1)  # column-based

newarrhsplit = np.hsplit(arr, 2)  # cannot adjust automatically, same as normal split
newarrvsplit = np.vsplit(arr, 3)
#newarrdsplit = np.dsplit(arr, 3) dsplit only works on 3 or more dimensions

print(newarr)
for x in newarr:
    print(x)

print(newarr1)
for x in newarr1:
    print(x)

print(newarrhsplit)
for x in newarrhsplit:
    print(x)

print(newarrvsplit)
for x in newarrvsplit:
    print(x)

# array search: where()
arr = np.array([1, 2, 3, 4, 4])
x = np.where(arr == 4)
y = np.where(arr % 2 == 0)
z = np.where(arr % 2 != 0)
m = np.where(arr % 2 == 1)
print(x,y,z,m)
#array searchsorted()
indexdefault=np.searchsorted(arr,4)
indexright=np.searchsorted(arr,4,side='right')
print(indexdefault,indexright)

multipleindexes=np.searchsorted(arr,[2,4])
print(multipleindexes)

# array sort()
arr = np.array([1, 2, 1, 4, 2])
print(np.sort(arr))

arrstring = np.array(["apple", 'peach', 'orange'])
print(np.sort(arrstring))

arrboolean=np.array([True,False,True])
print(np.sort(arrboolean))

arr2d=np.array([[4,1,5,2],[3,5,9,2]])
arr2de=np.array([[3,5,9,2],[4,1,5,2]])
print(np.sort(arr2d))
print(np.sort(arr2de))

# array filtering: using boolean index list
arr = np.array([2, 54, 32, 45])
x = [False, True, True, True]
newarr = arr[x]
print(newarr)
# creating an array with a filtering function
arr = np.array([1, 23, 453, 32, 89])

filterdirect_arr = arr % 2 != 0

filter_arr = []
for x in arr:
    if x % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]
newarrdirect = arr[filterdirect_arr]

print(filter_arr)
print(newarr)
print(newarrdirect)

from numpy import random
randomint=random.randint(100)#随机整型数
randomarray1d=random.randint(100,size=(5))#随机1d数组
randomarray2d=random.randint(100,size=(3,5))#随机2d数组
randomfloat=random.rand()#随机浮点数
randomfloat1d=random.rand(5)#随机浮点数1d数组
randomfloat2d=random.rand(3,5)#随机浮点数2d数组

print(randomint)
print(randomarray1d)
print(randomarray2d)
print(randomfloat)
print(randomfloat1d)
print(randomfloat2d)

x=random.choice([3,6,7,2,4,0])
xarray=random.choice([3,6,7,2,4,0],size=(3,5))
print(x)
print(xarray)
'''
#ufuncs
#adding two arrays
x=[1,2,3,4]
y=[8,7,6,5]

print(list(zip(x,y)))
z=[]

for i,j in zip(x,y):#for loop
    z.append(i+j)
print(z)

z1=np.add(x,y)#ufunc: add:replace iteration operations by vector-based operations to optimize the performance
print(z1)