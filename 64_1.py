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

lrewersow=0
czmax=0
for i in range(200):
    lczarnych=0
    for j in range(20):
        for k in range(20):
            if obrazki[i][j][k]=='1':
                lczarnych+=1
    if lczarnych>czmax:
        czmax=lczarnych
    if lczarnych > 200:
        lrewersow+=1

print(lrewersow)
print(czmax)