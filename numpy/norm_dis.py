#正規分布

import numpy as np
import matplotlib.pyplot as plt

def nd(x,mu,sigma): #mu:期待値、sigma:標準偏差
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(x-mu)**2/(2*sigma**2))

x = np.linspace(-5,5)
y1 = nd(x,0.0,0.5)
y2 = nd(x,0.0,1.0)

plt.plot(x,y1,label="σ:0.5",linestyle="dashed")
plt.plot(x,y2,label="σ:1.0",linestyle="solid")

plt.xlabel("x",size=14)
plt.ylabel("y",size=14)
plt.grid()

plt.show()
