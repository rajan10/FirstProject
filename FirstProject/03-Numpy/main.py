import numpy as np
arr=np.array([[1, 2, 3,60], 
              [4, 5, 6,70], 
              [7, 8, 9,80]])
ar=np.array([1,2,34,5])
list_data=[1,2,3,0,4]
print(arr*2)
print(list_data*2)
print(ar.ndim)
print(arr.ndim)
print(arr.shape)
print(ar.shape)  #returns a tuple of the dimensions of the array
print(arr.dtype)
print(np.array([1,2,3], dtype=np.float32))  #specifying the data type of the array
print(np.array([1,2,3,4,5])[0])
print(ar[-1])  #last element of the array
print(ar.size)  #returns the total number of elements in the array
print(arr[0:2])  #slicing the array