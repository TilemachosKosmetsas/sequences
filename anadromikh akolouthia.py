import matplotlib
import matplotlib.pyplot as plt

vx = []
vy = []
a1= 2

counter = 1
a2 = float(a1)

while counter <= 20:
    
    akol =   1 + 1/a2
    vx.append(counter)
    vy.append(float(akol))
    counter +=1
    a2=akol
    print (a2)
plt.plot(vx,vy,'ro')
plt.ylabel('ypsos')
plt.xlabel('oroi akolouthias')
plt.show()


#a(n+1) = an^2+1/3







        
