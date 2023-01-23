odczyt=[]
with open('dane_obrazki.txt') as file:
    for line in file:
        czyst=line.rstrip()
        odczyt.append(czyst)

obrazki=[]
n=0
for i in range(200):
    obrazekX = []
    for j in range(21):
        obrazekX.append(odczyt[n])
        n+=1
    obrazki.append(obrazekX)
    n+=1

poprawne=0
naprawialne=0
nienaprawialne=0
lmax=0
for i in range(200):
    licznikzle1=0
    licznikzle2=0
    for j in range(20):
        ljedynek=0
        for k in range(20):
            if obrazki[i][j][k] == '1':
                ljedynek+=1
        if ljedynek%2!=int(obrazki[i][j][20]):
            licznikzle1 += 1

    for j in range(20):
        ljedynek=0
        for k in range(20):
            if obrazki[i][k][j] == '1':
                ljedynek+=1
        if ljedynek%2!=int(obrazki[i][20][j]):
            licznikzle2 += 1
    if licznikzle1==0 and licznikzle2==0:
        poprawne+=1
    elif licznikzle1<=1 and licznikzle2<=1:
        naprawialne+=1
    else:
        nienaprawialne+=1
    if licznikzle1+licznikzle2>lmax:
        lmax=licznikzle1+licznikzle2

print(poprawne)
print(naprawialne)
print(nienaprawialne)
print(lmax)