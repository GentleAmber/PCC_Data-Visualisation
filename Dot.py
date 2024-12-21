import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-pastel')
y_values=list()
x_values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
y_values.append(x**2 for x in x_values)
fig, ax=plt.subplots()
ax.scatter(x_values,y_values,s=10)

plt.show()