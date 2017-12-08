from scipy.special import *
import numpy as np 
import matplotlib.pyplot as plt 

zz = np.linspace(0, 10000, 2000)
plt.figure(1)

plt.plot(zz, np.log(zz), 'b', label = 'log')
plt.plot(zz, digamma(zz), 'r', label = 'digamma')
plt.legend()

# plt.savefig('digamma_log.png')
plt.show()
