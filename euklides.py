def euod(a, b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a

def eumod(a, b):
    while b != 0:
        c = a%b
        a=b
        b=c
    return a

def eurek(a,b):
    while b!=0:
        c=a%b
        return eurek(b,c)
    return a


m, n = input('>  ').split()
m, n = int(m), int(n)
print(eurek(m,n))