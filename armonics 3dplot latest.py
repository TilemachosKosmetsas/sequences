from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax= fig.add_subplot(111, projection ='3d')

x = []
y = []
z = []

counter=1
while counter <=10:
    x.append(counter)
    y.append(1/counter)
    z.append(counter+3/counter)
    counter +=1
    
ax.scatter(x,y,z, c='r', marker='o')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()


