with open('tekst.txt') as file:
    for line in file:
        slowa=line.rstrip().split()


for slowo in slowa:
    if slowo[0]=='d' and slowo[len(slowo)-1]=='d':
        print(slowo)