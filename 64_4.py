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

for i in range(200):
    licznikzle1=0
    licznikzle2=0
    a=0
    b=0
    for j in range(20):
        ljedynek=0
        for k in range(20):
            if obrazki[i][j][k] == '1':
                ljedynek+=1
        if ljedynek%2!=int(obrazki[i][j][20]):
            licznikzle1 += 1
            a=j+1

    for j in range(20):
        ljedynek=0
        for k in range(20):
            if obrazki[i][k][j] == '1':
                ljedynek+=1
        if ljedynek%2!=int(obrazki[i][20][j]):
            licznikzle2 += 1
            b=j+1

    if licznikzle1<=1 and licznikzle2<=1 and licznikzle1+licznikzle2>0:
        if a==0:
            print(f'{i+1} {b},21')
        elif b==0:
            print(f'{i+1} 21,{a}')
        else:
            print(f'{i+1} {a},{b}')