from scipy.interpolate import interp1d
import numpy as np

xs=np.arange(10)
ys=2*xs+1
interf=interp1d(xs,ys)
ar=interf(np.arange(2.1,3,0.1))
print(ar)

