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

licznik=0
for i in range(200):
    lzlych=0
    for j in range(10):
        for k in range(10):
            if obrazki[i][j][k] != obrazki[i][j][k+10] or obrazki[i][j][k] != obrazki[i][j+10][k] or obrazki[i][j][k] != obrazki[i][j+10][k+10]:
                lzlych+=1
    if lzlych==0:
        licznik+=1
    if licznik==1:
        for j in range(20):
            print(obrazki[i][j][:20])

print(licznik)