odczyt = []
with open('bledne.txt') as file:
    for line in file:
        a = line.rstrip()
        odczyt.append(a)

ciagi = []
dlugosci = []
n = 0
while n<40:
    ciagitemp = []
    ciagitemp2 = []
    if n%2 == 0:
        dlugosci.append(int(odczyt[n]))
    else:
        ciagitemp = odczyt[n].split()
        for item in ciagitemp:
            ciagitemp2.append(int(item))
        ciagi.append(ciagitemp2)
    n+=1

r=[]
for i in range(20):
    rtemp = []
    a = ciagi[i][1] - ciagi[i][0]
    rtemp.append(a)

    b = ciagi[i][2] - ciagi[i][1]
    if b not in rtemp:
        rtemp.append(b)
    else:
        r.append(b)

    c = ciagi[i][3] - ciagi[i][2]
    if c not in rtemp:
        rtemp.append(c)
    elif a!=b:
        r.append(c)

    d = ciagi[i][4] - ciagi[i][3]
    if d not in rtemp:
        rtemp.append(d)
    elif a!=b and a!=c and b!=c:
        r.append(d)

bledne=[]
for j in range(20):
    for i in range(0,len(ciagi[j])):
        if i==0:
            if ciagi[j][i]+r[j]!=ciagi[j][i+1] and ciagi[j][i+1]+r[j]==ciagi[j][i+2]:
                bledne.append(ciagi[j][i])
                break
        elif i==len(ciagi[j])-1:
            if ciagi[j][i]-r[j]!=ciagi[j][i-1] and ciagi[j][i-1]-r[j]==ciagi[j][i-2]:
                bledne.append(ciagi[j][i])
                break
        else:
            if ciagi[j][i]-r[j]!=ciagi[j][i-1]:
                bledne.append(ciagi[j][i])
                break

print(bledne)