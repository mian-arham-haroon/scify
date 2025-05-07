import numpy as np
# from scipy.sparse.csgraph import connected_components
# from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall,bellman_ford
from scipy.sparse import csr_matrix


x=np.array([[0,0,0],[0,0,-1],[1,0,2]])
sh=csr_matrix(x)
# print(floyd_warshall(sh,return_predecessors=True,))
print(bellman_ford(sh,return_predecessors=True,indices=0))

# print(dijkstra(sh,return_predecessors=True,indices=0))
# print(connected_components(sh))

