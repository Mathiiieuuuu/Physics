from math import *

def f(v):
    return (v**(2)*exp(-(B*m/2)*v**2))

def integral(a,b,n): #méthode des trapèzes
    S=0
    for k in range(1,n+1):
        S=S+(b-a)/(2*n)*(f(a+(k-1)*(b-a)/n)+f(a*k*(b-a)/n))
    return S
    
#Constantes
m=2*1.67*10**(-27)
kb=1.38*10**(-23)
T=53
M=1.29*10**(22)
G=6.67*10**(-11)
R=1188000
B=1/(kb*T)


#Vitesse de libération
vl=sqrt(2*G*M/R)
print("vl =",vl,"m/s")

#Probabilité d'échappement d'une molécule
a=0
b=vl
n=100000

Prob=(1-(m*B/(2*pi))**(3/2)*8*pi*integral(a,b,n))*100

print("Proba =",Prob,"%")

