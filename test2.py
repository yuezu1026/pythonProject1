import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4,5]
x = np.arange(200)
y=[i*i for i in x]
print(y)

plt.plot(x,y)
plt.savefig('result.png')
plt.show()