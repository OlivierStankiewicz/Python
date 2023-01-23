hasla=[]
with open('hasla.txt') as file:
    for line in file:
        czyst=line.rstrip()
        hasla.append(czyst)

licznik=0
for haslo in hasla:
    l=0
    for znak in haslo:
        if ord(znak)>=ord('0') and ord(znak)<=ord('9'):
            l+=1
            break

    for znak in haslo:
        if ord(znak)>=ord('a') and ord(znak)<=ord('z'):
            l+=1
            break

    for znak in haslo:
        if ord(znak)>=ord('A') and ord(znak)<=ord('Z'):
            l+=1
            break

    if l==3:
        licznik+=1

print(licznik)
