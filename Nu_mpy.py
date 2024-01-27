import numpy as np

print(np.arange(1,10,2))
print(np.zeros(3))
a=np.ones((3,3),dtype=int)
print(np.arange(10).reshape(2,5))
arr1=np.arange(3)
arr2=np.arange(3)
print(np.concatenate([arr1,arr2],axis=0))

e=np.vstack([arr1,arr2])
f=np.hstack([arr1,arr2])
print(e,f)