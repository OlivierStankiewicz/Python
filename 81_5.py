def d(t):
    w1=t[4]-t[2]
    w2=t[5]-t[3]
    d=[t[0]+w1, t[1]+w2]
    return d


wsp=[]
with open('wspolrzedneTR.txt') as file:
    for line in file:
        czyst=line.rstrip().split()
        wsp.append(czyst)

for line in wsp:
    for i in range(len(line)):
        line[i]=int(line[i])

for line in wsp:
    if d(line)[0]==d(line)[1]:
        print(f'{line}{d(line)}')