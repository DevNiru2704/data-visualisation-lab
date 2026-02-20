import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
values = []

for label in labels:
    val = int(input(f"Enter value for {label}: "))
    values.append(val)

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Dynamic Pie Chart")

plt.show()