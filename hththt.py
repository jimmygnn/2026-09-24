import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 1000)
y = 1 - 0.5 * np.abs(x - 2)
width = (x + 1) ** 2
plt.scatter(x, y, s=width, color='lime')
plt.show()