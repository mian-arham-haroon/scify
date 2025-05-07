from scipy.sparse import csr_matrix
import numpy as np

x=np.array([[0,0,0],[0,0,1],[1,0,2]])
y=csr_matrix(x).tocsc()
print(y)
# z=(csr_matrix(x))
# z.eliminate_zeros
# z.sum_duplicates
# print(z)
# print(csr_matrix(x).count_nonzero())
# print(csr_matrix(x).data)











# x=np.array([0,0,0,0,0,4,0,0,3,0,0,0,0,8])print(csr_matrix(x))


