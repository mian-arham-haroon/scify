from scipy.interpolate import interp1d,UnivariateSpline,Rbf
import numpy as np

xs=np.arange(10)
# ys=2*xs+1
ys=xs**2+np.arange(10)+1
# interf=interp1d(xs,ys)
interf=Rbf(xs,ys)
ar=interf(np.arange(2.1,3,0.1))
print(ar)

