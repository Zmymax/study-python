import numpy as np

a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
#从某个索引处开始切割
print('从数组索引 a[1:] 处开始切割')
print(a[1:])
print("-----------------")
print(a[...,0])
print(a[0,...])
print(a[...,1:])
