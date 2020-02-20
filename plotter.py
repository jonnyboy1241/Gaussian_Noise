import matplotlib.pyplot as plt
import numpy as np
import gaussian_noise

x_values, y_values = gaussian_noise.generate_data(0, 2*np.pi, 100, np.pi/16)

plt.scatter(x_values, y_values, s=50, facecolors='none', edgecolors='b')
x_cont = np.arange(-2.0, 12.0, .01)
#plt.plot(x_cont, np.sin(3*x_cont-np.pi/2), 'k')
plt.axis([-np.pi/2, 5*np.pi/2, -1.5, 1.5])
plt.show()
