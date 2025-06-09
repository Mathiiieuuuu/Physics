from vpython import *
#Web VPython 3.2
canvas(width=1920, height=1080, background=color.black)
#Mass of Bodies
Msoleil=2*10**30
Mterre=6*10**24
M1=random(1,300)*Msoleil
M2=random(1,300)*Msoleil
M3=random(1,300)*Msoleil
m=[M1,M2,M3]

#Gravitational constant
G=6.67*10**(-11)

#Anti-collider system
rc=0.5

#Distance from the origin (0.0.0)
dmoyen=20000000000
d1=vector(random(-5,7)*dmoyen,0,0)
d2=vector(0,random(-5,7)*dmoyen,0)
d3=vector(0,0,random(-5,7)*dmoyen)


#Size of Bodies
rsoleil=696340000
r1=rsoleil*(1+0.1*random(1,200))
r2=rsoleil*(1+0.1*random(1,200))
r3=rsoleil*(1+0.1*random(1,200))


#Bodies configuration
a=True
stars=[]
stars[0]=sphere(pos=d1,radius=r1,make_trail=a,color=color.yellow) #0
stars[1]=sphere(pos=d2,radius=r2,make_trail=a,color=color.red) #1
stars[2]=sphere(pos=d3,radius=r3,make_trail=a,color=color.orange) #2


#Force and Velocity
vmoyen=5000
p=[]
v=[vector(0,random(1,30)*vmoyen,0),vector(0,0,random(1,30)*vmoyen),vector(random(1,30)*vmoyen,0,0)]
F=[]

#Momentum
for i in range(len(stars)):
   p[i] = m[i]*v[i]
   F[i] = vector(0,0,0)
  
#Conservation of Momentum in a gravitational field
t = 0
dt = 10

while t<100000000000:
  rate(10000)
  for i in range(len(stars)):
    F[i]=vector(0,0,0)
  for i in range(len(stars)):
    for j in range(len(stars)):
      if i!=j:
        rji = stars[i].pos - stars[j].pos
        F[i] = F[i] - G*m[i]*m[j]*norm(rji)/(mag(rji)**2+rc**2)
        
  for i in range(len(stars)):
    p[i] = p[i] + F[i]*dt
    stars[i].pos = stars[i].pos + p[i]*dt/m[i]
  t = t + dt