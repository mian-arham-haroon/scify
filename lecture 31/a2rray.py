from scipy import io 
import numpy as np

ar=np.arange(10)
io.savemat('ar.mat',{'vec':ar})
arn=io.loadmat('ar.mat',squeeze_me=True)
print(arn['vec'],)
