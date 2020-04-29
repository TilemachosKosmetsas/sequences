import matplotlib
import matplotlib.pyplot as plt

vx = []
vy = []
vz=[]
a1 = input("dwse ton prwto oro tis akolouthias \n")
v1 = input("dwse tin stathera n tis akolouthias \n")
counter = 1
a2 = int(a1)
v2= float(v1)
while counter <= 10:
    
    akol =  (1/((1/a2)+(counter-1)*v2))
    vx.append(counter)
    vy.append(akol)
    counter +=1
    
plt.plot(vx,vy,vz,'ro')
plt.ylabel('ypsos')
plt.xlabel('oroi akolouthias')
plt.show()


'''
while 0<n < 5:

an = 1

'''
a1 = toso





        
