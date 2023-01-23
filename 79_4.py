import math

def roznica(t1, t2):
    x1, y1 = float(t1[0]), float(t1[1])
    x2, y2 = float(t2[0]), float(t2[1])

    wyn=math.sqrt((x1-x2)**2+(y1-y2)**2)
    return wyn

def czy_wsp(t1, t2):
    x1, y1, r1 = float(t1[0]), float(t1[1]), float(t1[2])
    x2, y2, r2 = float(t2[0]), float(t2[1]), float(t2[2])
    odl=roznica(t1,t2)

    if odl <= r1+r2 and odl>=abs(r1-r2):
        return True
    return False


okregi=[]
with open('okregi.txt') as file:
    for line in file:
        czyst=line.rstrip().split()
        okregi.append(czyst)

ciagmax=0
ciagtemp=1

for i in range(len(okregi)-1):
    if czy_wsp(okregi[i], okregi[i+1]):
        ciagtemp+=1
        if ciagtemp>ciagmax:
            ciagmax=ciagtemp
    else:
        ciagtemp=1

print(ciagmax)