def czy_1(x,y):
    if x>0 and y>0:
        return True
    return False

wsp=[]
with open('wspolrzedne.txt') as file:
    for line in file:
        czyst=line.rstrip().split()
        wsp.append(czyst)

for line in wsp:
    for i in range(len(line)):
        line[i]=int(line[i])

licznik=0
for line in wsp:
    for i in range(3):
        if not(czy_1(line[2*i],line[2*i+1])):
            break
    else:
        licznik+=1

print(licznik)