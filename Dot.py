import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-pastel')
x_values=range(1,1001)
y_values=[x**2 for x in x_values]
fig, ax=plt.subplots()
#ax.scatter(x_values,y_values,color=(0,0.8,0),s=10)
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)
ax.axis([0,1100,0,1100000])
plt.show()