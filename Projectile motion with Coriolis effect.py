import numpy as np
import matplotlib.pyplot as plt
import matplotlib.inline

M = 1.0
g = 9.8
V = 80
ang = 60.0
Cd = 0.005
dt = 0.5

print V, ang

t = [0]
vx = [V*np.cos(ang/180*np.pi)]
vy = [V*np.sin(ang/180*np.pi)]
x = [0]
y = [0]

drag=Cd*V**2 
ax = [-(drag*np.cos(ang/180*np.pi))/M ]          
ay = [-g-(drag*np.sin(ang/180*np.pi)/M) ]

dt = 0.2

counter = 0
while (y[counter] >= 0):
    t.append(t[counter]+dt)
    
    vx.append(vx[counter]+dt*ax[counter])
    vy.append(vy[counter]+dt*ay[counter])
    x.append(x[counter]+dt*vx[counter])    
    y.append(y[counter]+dt*vy[counter])    
    vel = np.sqrt(vx[counter+1]**2 + vy[counter+1]**2)
    drag = Cd*vel**2
    ax.append(-(drag*np.cos(ang/180*np.pi))/M)     
    ay.append(-g-(drag*np.sin(ang/180*np.pi)/M))
    counter = counter +1
plt.plot(x,y,'ro')
plt.ylabel("y (m)")
plt.xlabel("x (m)")

print "Range of projectile is {:3.1f} m".format(x[counter])