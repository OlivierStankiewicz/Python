def czy_trojk(t):
    k = sorted(t)
    if k[0]**2 + k[1]**2 == k[2]**2:
        return True
    return False


trojki=[]
with open ('trojki.txt') as file:
    for line in file:
        t=line.rstrip().split()
        for i in range(3):
            t[i] = int(t[i])
        trojki.append(t)

for i in range(len(trojki)-1):
    if czy_trojk(trojki[i]) and czy_trojk(trojki[i+1]):
        print(trojki[i])
        print(trojki[i+1])