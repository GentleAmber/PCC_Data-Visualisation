import matplotlib.pyplot as plt
squares=list()
input_value=list()
for x in range(1,6):
    squares.append(x**2)
    input_value.append(x)
plt.style.use('seaborn-v0_8-pastel')
fig, ax= plt.subplots()
ax.plot(input_value,squares, linewidth=3)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value",fontsize=14)
ax.tick_params(labelsize=14)

plt.show()