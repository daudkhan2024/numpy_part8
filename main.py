import numpy as np
print("Iterating Numpy Array")
x = np.array([1,2,3,4])
print(x)
for i in x:
    print(i)

print("if its 2D array")
x2 = np.array([[1,2,3,4],[1,2,3,4]])
print(x2)
print()
for j in x2:
    print(j)

print()
for k in x2:
    for l in  k:
        print(l)


print()
print("for 3d" )
x3 = np.array([[[1,2,3],[4,5,6],[6,7,8]]])
print(x3.ndim)
print()

for i  in x3:
    for j in i:
        for k in j:
            print(k)

print()
print("if we not want to use forloop all time we can use  "
      "another funtion  np.nditer()")
for i in np.nditer(x3):
    print(i)

print()
print("another way to store this iterated data is ")
for i in np.nditer(x3,flags=['buffered'],op_dtypes=["S"]):
    print(i)


print()
print("if i want to show data with its index  ndenumerate()")
for i,d in np.ndenumerate(x3):
    print(i,d)