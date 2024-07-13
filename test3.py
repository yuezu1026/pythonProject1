import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = np.linspace(-10,10,100)

X,Y = np.meshgrid(x,y)


print(x)
print(y)

print(X.shape)
print(Y.shape)

Z = np.sqrt(X**2+Y**2)

#plt.contourf(X,Y,Z) #画等高线图
plt.contour(X,Y,Z)
plt.show()

