def reszta(t,n):
    monety={}
    for i in t:
        while n>=i:
            n-=i
            if i not in monety:
                monety[i]=1
            else:
                monety[i]+=1
    return monety

t=[500,200,100,50,20,10,5,2,1]
cena=int(input('> '))
print(reszta(t,cena))