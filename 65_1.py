ulamki=[]
with open('dane_ulamki.txt') as file:
    for line in file:
        utemp=[]
        a,b=line.rstrip().split()
        utemp.append(int(a))
        utemp.append(int(b))
        ulamki.append(utemp)

l=ulamki[0][0]
m=ulamki[0][1]
mini=ulamki[0][0]/ulamki[0][1]
for i in ulamki:
    if i[0]/i[1] < mini:
        mini=i[0]/i[1]
        m=i[1]
        l=i[0]

    elif i[0]/i[1] == mini and i[1]<m:
        m=i[1]
        l=i[0]

print(l)
print(m)