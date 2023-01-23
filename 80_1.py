def prost(a,b,c):
    t=[a,b,c]
    t.sort()
    if t[0]**2 + t[1]**2 == t[2]**2:
        return True
    return False


trojk=[]
with open('dane_trojkaty.txt') as file:
    for line in file:
        czyst=int(line.rstrip())
        trojk.append(czyst)

for i in range(len(trojk)-2):
    if prost(trojk[i], trojk[i+1], trojk[i+2]):
        print(f'{trojk[i]} {trojk[i+1]} {trojk[i+2]}')