def rozklad(a):
    t=[]
    n=2
    while a>1:
        while a%n==0:
            a/=n
            t.append(n)
        n+=1
    return t

l=input('> ')
print(rozklad(int(l)))