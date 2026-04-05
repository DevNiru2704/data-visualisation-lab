import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = -x + np.random.normal(0, 0.1, 50)
x = np.append(x, 0.2)
y = np.append(y, 2)
plt.scatter(x, y, color='blue', label='Data Points')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Negative Correlation with Outlier")
plt.show()