import math
import numpy as np

def euclidean_distance(x1,x2):
  """Euclidean distance between two points"""
  return np.linalg.norm(x1-x2)

list1=np.array([1,2,3])
list2=np.array([3,4,5])
res=euclidean_distance(list1,list2)
print(res)
