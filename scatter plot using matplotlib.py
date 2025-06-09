import matplotlib.pyplot as plt
g = [81,90,70,89,100,80,90,100,80,34]
b = [30,29,49,48,100,48,34,45,20,30]
gr = [10,20,30,40,50,60,70,80,90,100]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.scatter(gr,g,color = 'r')
ax.scatter(gr,b,color = 'b')
ax.set_xlabel('Grades scored')
ax.set_ylabel('Grades scored')
ax.set_title('Scatter plot')
plt.show()
