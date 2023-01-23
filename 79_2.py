def lustrzane(t1,t2):
    if t1[2] != t2[2]:
        return False

    x1, y1 = float(t1[0]), float(t1[1])
    x2, y2 = float(t2[0]), float(t2[1])

    if x1==x2 and y1==-y2:
        return True
    if x1==-x2 and y1==y2:
        return True
    return False


okregi=[]
with open('okregi.txt') as file:
    for line in file:
        czyst=line.rstrip().split()
        okregi.append(czyst)

licznik=0

for i in range(len(okregi)):
    for j in range(i,len(okregi)):
        if lustrzane(okregi[i], okregi[j]):
            licznik+=1

print(licznik)