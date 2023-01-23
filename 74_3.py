def czy_kolejne(a,b,c,d):
    t=[a,b,c,d]
    t.sort()
    if ord(t[0])+1 == ord(t[1]) and ord(t[1])+1 == ord(t[2]) and ord(t[2])+1 == ord(t[3]):
        return True
    return False


hasla=[]
with open('hasla.txt') as file:
    for line in file:
        czyst=line.rstrip()
        hasla.append(czyst)

licznik=0
for haslo in hasla:
    for i in range(len(haslo)-3):
        if czy_kolejne(haslo[i], haslo[i+1], haslo[i+2], haslo[i+3]):
            licznik+=1
            break

print(licznik)