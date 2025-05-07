from scipy.spatial import Delaunay
import numpy as np
import matplotlib.pyplot as plt

a=np.array([[1,2],[3,1],[4,2],[2,2],[4,1]])
s=Delaunay(a).simplices
plt.triplot(a[:,0],a[:,1],s)
plt.scatter(a[:,0],a[:,1],color='r')



plt.show()