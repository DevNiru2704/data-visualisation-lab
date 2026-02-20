import matplotlib.pyplot as plt

data = list(map(int,input("Enter data values:").split()))
plt.hist(data, bins=5)
plt.xlabel("Data values")
plt.ylabel("Frequency")
plt.title("Simple Histogram")
plt.show()