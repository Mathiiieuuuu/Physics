import math

def double_fact(n):
    p=1
    if n%2==0:
        for i in range(2,n+1,2):
            p=p*i
    if n%2!=0:
        for i in range(1,n+1,2):
            p=p*i
    return p
        

def elliptic(n,k):
    s=1
    for i in range(1,n+1):
        s=s+(double_fact(2*i-1)/double_fact(2*i))**2*k**(2*(i))
    return s

l=float(input("Longueur du fil ?:  "))
g=float(input("Pesanteur ?:  "))
teta0=float(input("Angle initial ?:  "))
n=int(input("Degré de precision ?:  "))

k=math.sin((teta0*math.pi)/360)
r=4*math.sqrt(l/g)

if k==1:
    print("infini")
else:
    T=r*(math.pi/2)*elliptic(n,k)
    print("La période de ce pendule est de ",T,"secondes !")