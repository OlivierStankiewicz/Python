liczby=[]
with open('liczby1.txt') as file:
    for line in file:
        a=line.rstrip()
        liczby.append(int(a,8))

lmax=liczby[0]
lmin=liczby[0]
for l in liczby:
    if l>lmax:
        lmax=l
    elif l<lmin:
        lmin=l

print(oct(lmin)[2:])
print(oct(lmax)[2:])