import matplotlib
import matplotlib.pyplot as plt

vx = []
vy = []
a1 = input("dwse ton prwto oro tis akolouthias \n")
v1 = input("dwse tin stathera n tis akolouthias \n")
counter = 1
a2 = int(a1)
v2= float(v1)
while counter <= 10:
    
    akol =  (a2+(counter-1)*v2) 
    vx.append(counter)
    vy.append(akol)
    counter +=1
'''    
plt.plot(vx,vy,'ro')
plt.ylabel('ypsos')
plt.xlabel('oroi akolouthias')
plt.show()
 # an thelw sxima na svisw tous tonous''' 


en= input("poion oro tis akolouthias thes na matheis\n")
en2= int(en)
print (a2+(en2-1)*v2)





        
