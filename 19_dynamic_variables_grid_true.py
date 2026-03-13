import matplotlib.pyplot as plt

X=list(map(int,input("Enter the elements of the list:").split()))
y=list(map(lambda x:x**2,X))

plt.plot(X,y,marker='o')
plt.xlabel("X values (independent)")
plt.ylabel("Dependent (dependent)")
plt.title("X-Y Axis Data Plot")
plt.grid(True)
plt.show()