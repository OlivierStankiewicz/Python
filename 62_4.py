liczby=[]
with open('liczby2.txt') as file:
    for line in file:
        czyst=line.rstrip()
        liczby.append(int(czyst))

a=0
b=0
for l in liczby:
    for c in str(l):
        if c=='6':
            a+=1

    for c in str(oct(l)):
        if c=='6':
            b+=1

print(a)
print(b)