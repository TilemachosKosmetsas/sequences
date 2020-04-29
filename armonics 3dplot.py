from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax= fig.add_subplot(111, projection ='3d')

x = [1,1.1,1.2]
y = [2,3,4]
z = [3]

ax.scatter(x,y,z, c='r', marker='o')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()


'''
a1 = 10
v = 0.002

for i in range (1,100):
        akol =  (1/((1/a1)+(i-1)*v)) 
        print ("a",i,"=",akol)

'''
