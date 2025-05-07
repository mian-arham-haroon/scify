import numpy as np
# from scipy.sparse.csgraph import connected_components
# from scipy.sparse.csgraph import dijkstra
# from scipy.sparse.csgraph import floyd_warshall,bellman_ford
from scipy.sparse.csgraph import floyd_warshall,bellman_ford,depth_first_order ,breadth_first_order
from scipy.sparse import csr_matrix


x=np.array([[0,1,0,1],[1,1,1,1],[2,1,2,1],[1,2,1,0]])
sh=csr_matrix(x)
# print(floyd_warshall(sh,return_predecessors=True,))
# print(depth_first_order(sh,1))
print(breadth_first_order(sh,1))

# print(dijkstra(sh,return_predecessors=True,indices=0))
# print(connected_components(sh))

