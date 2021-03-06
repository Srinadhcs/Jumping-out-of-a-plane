from re import X
from sqlite3 import Timestamp
from turtle import distance
import scipy.integrate
import matplotlib.pyplot as plt
import pickle
from math import exp


def f(t,g,vt):
    num=1-exp(-2*g*t/vt)
    den=1+exp(-2*g*t/vt)
    return num/den

# 2)
result =1400- 54*scipy.integrate.quad(lambda x: f(x,9.8,54.0),0.0,29.74519)[0]
print('q2 result:',result)
# 3)
distance_left=4000 # distance from the ground
positions=[] # position stamps
times=[] # time stamps
delta_time=1 # a time step
high_time=0
while(True):
    low_time=high_time
    high_time+=delta_time
    # I=Integral("(1-exp(-2*9.8*t/54))/(1+exp(-2*9.8*t/54))",(t,low_time,high_time)).evalf()
    I = scipy.integrate.quad(lambda x: f(x,9.8,54),low_time,high_time)[0]
    times.append(high_time)
    positions.append(distance_left-I)
    distance_left-=I
    if(positions[-1]<0):
        times.pop(-1)
        positions.pop(-1)
        break


plt.plot(times,positions)
plt.show()
with open('q3.pickle','wb') as f:
    pickle.dump((times,positions),f)

# 4)
'''
rate of change of terminal velocity = (54-7.6)/3 = 15.467 m/s**2
v-u = a*t
so t=(10**-6)/15.467 = 6.4654 * 10**-8 sec

'''
def timestep(v,u,t,deltaV):
    a=(v-u)/t
    return (deltaV)/a

print(timestep(54,7.6,3,10**-6))

# 5)
def terminal_velocity(t):
    return 54-15.47*t

## x=integrate: v dt, from t=0 to t=3
delta=0.001
high=0
result=0
timestamp=[]
positionstamp=[]
for _ in range(int(3/delta)):
    low=high
    high=delta
    this_distance = scipy.integrate.quad(lambda x: terminal_velocity(x),low,high)[0]
    result+=this_distance
    timestamp.append(low)
    positionstamp.append(result)
print('q5', result)

# 6)
x=timestamp 
y=positionstamp
plt.plot(x,y)
plt.show()
with open('q6.pickle','wb') as f:
    pickle.dump((x,y),f)
