liczby=[]
with open('liczby.txt') as file:
    for line in file:
        a=line.rstrip()
        liczby.append(int(a))

for item in liczby:
    dzielniki = []
    i=1
    while i<=item:
        if item%i == 0:
            dzielniki.append(i)
        i+=1
    if len(dzielniki) == 18:
        print(item)
        print(dzielniki)