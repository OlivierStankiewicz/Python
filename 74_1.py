hasla=[]
with open('hasla.txt') as file:
    for line in file:
        czyst=line.rstrip()
        hasla.append(czyst)

cyfry = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
licznik=0

for item in hasla:
    for znak in item:
        if znak not in cyfry:
            break
    else:
        licznik+=1

print(licznik)