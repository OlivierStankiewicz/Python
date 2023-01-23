liczby1=[]
with open('liczby1.txt') as file1:
    for line in file1:
        czyst=line.rstrip()
        liczby1.append(int(czyst,8))

liczby2=[]
with open('liczby2.txt') as file2:
    for line in file2:
        czyst=line.rstrip()
        liczby2.append(int(czyst))

a=0
b=0
for i in range(1000):
    if liczby1[i]==liczby2[i]:
        a+=1
    elif liczby1[i]>liczby2[i]:
        b+=1

print(a)
print(b)