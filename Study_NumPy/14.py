import numpy as np

#使用range函数创建列表对象
list=range(4)
it=iter(list)

#使用迭代器创建 ndarray
x=np.fromiter(it,dtype=float)
print(x)