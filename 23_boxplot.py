import matplotlib.pyplot as plt

weights = [25, 28, 29, 29, 30, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
plt.boxplot(weights)
plt.xlabel("Weights")
plt.title("Box Plot of Weights")
plt.show()