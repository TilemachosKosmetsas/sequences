import matplotlib
import matplotlib.pyplot as plt

vx = []
vy = []
n = 1

while n <= 30:
    
    akol =  (3*(n**2)+2*n-1)/(2*(n**2)-n+2) 
    vx.append(n)
    vy.append(akol)
    n +=1
    
plt.plot(vx,vy,'ro')
plt.ylabel('ypsos')
plt.xlabel('oroi akolouthias')
plt.show()






        
