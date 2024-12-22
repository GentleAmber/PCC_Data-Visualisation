import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# One figure
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')
plt.savefig('SimplePlot.png')

# Two figures?
f, (ax1, ax2) = plt.subplots(1, 2,sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)
plt.savefig('SharingYaxis.png')

# Create four polar Axes and access them through the returned array
fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)
plt.savefig("FourPolar.png")