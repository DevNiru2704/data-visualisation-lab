import matplotlib.pyplot as plt

X=[1,2,3,4,5,6,7,8,9,10]
y=[10,20,15,30,40,50,60,70,80,90]

plt.plot(X,y,marker='o')
plt.xlabel("X values (independent)")
plt.ylabel("Dependent (dependent)")
plt.title("X-Y Axis Data Plot")
plt.grid(True)
plt.show()