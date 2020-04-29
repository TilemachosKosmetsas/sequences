import matplotlib
import matplotlib.pyplot as plt
import numpy as np
vx = []
vy = []
a1= 1

counter = 1
a2 = float(a1)

while counter <= 200:
    
    akol =   0.5 + 0.02*counter + a2 + np.random.normal(0,1)
    vx.append(counter)
    vy.append(float(akol))
    counter +=1
    a2=akol
    print (a2)
    print(np.random.normal(0,1))
plt.plot(vx,vy,'ro')
plt.ylabel('ypsos')
plt.xlabel('oroi akolouthias')
plt.show()











        
