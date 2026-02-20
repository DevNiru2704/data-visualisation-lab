import matplotlib.pyplot as plt

n = int(input("Enter number of data points: "))
x = []
y = []

for i in range(n):
    x_val = int(input("Enter x value: "))
    y_val = int(input("Enter y value: "))
    x.append(x_val)
    y.append(y_val)

plt.plot(x, y)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Dynamic Line Chart")
plt.show()