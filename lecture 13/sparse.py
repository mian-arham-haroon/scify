from scipy.sparse import csr_matrix
import numpy as np

x=np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(x).count_nonzero())
# print(csr_matrix(x).data)











# x=np.array([0,0,0,0,0,4,0,0,3,0,0,0,0,8])print(csr_matrix(x))


