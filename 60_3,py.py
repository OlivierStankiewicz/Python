liczby=[]
with open('liczby.txt') as file:
    for line in file:
        a = line.rstrip()
        liczby.append(int(a))


dzielniki=[]
for item in range(200):
    dzielnikitemp = []
    i = 2
    while i <= item:
        if item % i == 0:
            dzielnikitemp.append(i)
        i += 1
    dzielniki.append(dzielnikitemp)

najwl=0
for i in range(200):
    czy=False
    for dzielnik in dzielniki[i]:
        for j in range(200):
            if j!=i:
                if dzielnik in dzielniki[j]:
                    czy=True
    if not czy and liczby[i]>najwl:
        najwl=liczby[i]
        print(najwl)
