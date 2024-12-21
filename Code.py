import numpy as np
import matplotlib.pyplot as plt

m=50
T=0.2
O=10000

b0=[1,1,1,1,1,1,1,1,1]

def roundt(dt):
    scale=10**(1-int(np.log10(dt)))
    return round(dt*scale,1)/scale

steps=int(O/len(b0))
dt=roundt(T/steps)
T=steps*dt

def Atob(A):
    b=np.empty(A.size,dtype=object)
    for i,a in enumerate(A):
        b[i]=[-2*z for z in a]
    return b

def b0toA0(b0):
    return [-x/2 for x in b0]
    
def simulate(A0,T,steps):
    N=len(A0)
    A=np.empty(N,dtype=object)
    for i,a in enumerate(A0):
        A[i]=[a]
    print("dt = ",dt)
    
    for i in range(steps):
        
        for n in range(N):
            s=0
            for n1 in range(-N,N+1):
                if n1==0:
                    continue
                for n2 in range(-N,N+1):
                    n3=n+1-n1-n2
                    if n3*n2==0 or abs(n3)>N:
                        continue
                    s-=np.sign(n1*n2*n3)*A[abs(n1)-1][i]*A[abs(n2)-1][i]*A[abs(n3)-1][i]
            A[n].append(A[n][i]+dt*((m-(n+1)**2)*A[n][i]-s))
    return A
        
def plotcoeffs(b):
    t=[dt*j for j in range(steps+1)]
    for i,bi in enumerate(b):
        plt.plot(t,bi,label=f"b{i+1}")
        plt.legend(loc='center right')
        plt.xlabel("time(s)")
        plt.title(f"m={m}, dt={dt}s")
        plt.tight_layout()

A0=b0toA0(b0)
A=simulate(A0,T,steps)
b=Atob(A)

plotcoeffs(b)
