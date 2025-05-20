import matplotlib.pyplot as plt
air=[168,190,170,178,195]
range=(160,200)
bins=5
plt.hist(air,bins,range,color='black',histtype='bar',rwidth=0.3)
plt.xlabel('City')
plt.ylabel('Air Quality Index')
plt.title('Histogram Plot')
plt.show()