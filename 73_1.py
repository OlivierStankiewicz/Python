with open('tekst.txt') as file:
    for line in file:
        slowa=line.rstrip().split()

licznik=0
for slowo in slowa:
    for i in range(len(slowo)-1):
        if slowo[i]==slowo[i+1]:
            licznik+=1
            break

print(licznik)