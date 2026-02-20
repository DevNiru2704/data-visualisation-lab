import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
line, = ax.plot(x, y, color='blue')
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Animated Line Graph")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
def animate(frame):
   line.set_ydata(np.sin(x + frame / 10))
   return line,
ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
plt.show()
