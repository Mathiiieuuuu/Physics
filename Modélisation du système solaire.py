from vpython import *
#Web VPython 3.2
canvas(width=1920, height=1080, background=color.black)
G=6.6743*10**(-11)
R=696340000
rs=0.02
###distance
Dv=107476000000
Dt=147098074000
Dma=206655000000
Dj=740680000000
Dm=46001200000
Ds=1349800000000
Du=2735000000000
Dn=4459800000000

###masse
Ms=1.989*10**30
Mv=4.867*10**24
Mt=5.974*10**24
Mma=6.417*10**23
Mj=1.898*10**27
Mm=3.285*10**23
Msa=5.683*10**26
Mu=8.681*10**25
Mn=1.024*10**26

a=True
stars=[0,0,0,0,0,0,0,0,0]
stars[0]=sphere(pos=vector(0,0,0),radius=12*R,make_trail=a,color=color.yellow) #SOLEIL
stars[1]=sphere(pos=vector(Dv,0,0),radius=7*R,make_trail=a,color=color.orange) #VENUS
stars[2]=sphere(pos=vector(Dt,0,0),radius=7*R,make_trail=a,color=color.blue) #TERRE
stars[3]=sphere(pos=vector(Dma,0,0),radius=7*R,make_trail=a,color=color.red) #MARS
stars[4]=sphere(pos=vector(Dj,0,0),radius=7*R,make_trail=a,color=color.red) #JUPITER
stars[5]=sphere(pos=vector(Dm,0,0),radius=7*R,make_trail=a,color=color.white) #MERCURE
stars[6]=sphere(pos=vector(Ds,0,0),radius=7*R,make_trail=a,color=color.orange) #SATURNE
stars[7]=sphere(pos=vector(Du,0,0),radius=7*R,make_trail=a,color=color.blue) #URANUS
stars[8]=sphere(pos=vector(Dn,0,0),radius=7*R,make_trail=a,color=color.white) #NEPTUNE


m=[Ms,Mv,Mt,Mma,Mj,Mm,Msa,Mu,Mn]
p=[0,0,0,0,0,0,0,0,0]
w=[vector(0,0,0),vector(0,3.24*10**(-7),0),vector(0,1.99*10**(-7),0),vector(0,1.06*10**(-7),0),vector(0,1.68*10**(-8),0),vector(0,8.267*10**(-7),0)]
v=[vector(0,0,0),vector(0,0,-35264.3),vector(0,0,-30290),vector(0,0,-26503),vector(0,0,-13720),vector(0,0,-58980),vector(0,0,-10180),vector(0,0,-7110),vector(0,0,-5500)]
F=[0,0,0,0,0,0,0,0,0]


for i in range(len(stars)):
    p[i] = m[i]*v[i]
    #p[i] = m[i]*cross(w[i],vector(stars[i].pos.x,0,stars[i].pos.z))
    F[i] = vector(0,0,0)

t = 0
dt =1000

while t<100000000000:
    rate(1000)
    for i in range(len(stars)):
        F[i]=vector(0,0,0)
    for i in range(len(stars)):
        for j in range(len(stars)):
            if i!=j:
                rji = stars[i].pos - stars[j].pos
                F[i] = F[i] - G*m[i]*m[j]*norm(rji)/(mag(rji)**2)
        
    for i in range(len(stars)):
        p[i] = p[i] + F[i]*dt
        stars[i].pos = stars[i].pos + p[i]*dt/m[i]
    t = t + dt
