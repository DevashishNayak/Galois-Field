#Galois Field
import numpy as np

p=int(input("Enter p"))
n=int(input("Enter n"))

g=[]
h=[]

f=p**n

def am(f,n):
    if n==1:
        for i in range(f):
            for j in range(f):
                x=(i+j)%f
                y=(i*j)%f
                g.append(x)
                h.append(y)
    else:
        for i in range(f):
            for j in range(f):
                x=bin(i).replace("0b", "")
                y=bin(j).replace("0b", "")
                z=int(x,2)^int(y,2)
                a=list(map(int, list(x)))
                b=list(map(int, list(y)))
                c=np.polymul(a,b)
                d=[1]*(n+1)
                if n%2==1:
                    d[n-1]=0
                q, r = np.polydiv(c, d)
                e =  [int(abs(k))%2 for k in r]
                l=list(map(str, e))
                m="".join(l)
                o=int(m,2)
                g.append(z)
                h.append(o)
    a=np.array(g).reshape(f,f)
    m=np.array(h).reshape(f,f)
    return a,m

a,m=am(f,n)
print(a)
print(m)
