import numpy as np
s1= b'Hello World'
a=np.frombuffer(s1,dtype='S1')
print(a)
