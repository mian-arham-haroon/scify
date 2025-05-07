from scipy.spatial import Delaunay,ConvexHull
import numpy as np
import matplotlib.pyplot as plt

a=np.array([[1,2],[3,1],[4,2],[2,2],[4,1],[1,3],[5,0],[3,1],[1,2],[0,2]])
hull=ConvexHull(a)
h_point=hull.simplices
plt.scatter(a[:,0],a[:,1])
for i in h_point:
    plt.plot(a[i,0],a[i,1],'k-')
plt.show()    
# s=Delaunay(a).simplices
# plt.triplot(a[:,0],a[:,1],s)
# plt.scatter(a[:,0],a[:,1],color='r')




plt.show()