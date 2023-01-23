liczby=[]
with open('liczby.txt') as file:
    for line in file:
        n=line.rstrip()
        liczby.append(int(n))

licznik=0
a=liczby[0]
b=a
for item in liczby:
    if item < 1000:
        licznik+=1
        b=a
        a=item

print(f'''{licznik}
{b}
{a}''')