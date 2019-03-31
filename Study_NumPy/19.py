import numpy as np

a=np.arange(10)
s=slice(2,7,2)
b=a[2:7:2]
print(a[s])
print(b)