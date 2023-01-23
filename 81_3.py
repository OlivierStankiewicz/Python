import math

def obw(t):
    ab=math.sqrt((t[0]-t[2])**2+(t[1]-t[3])**2)
    ac=math.sqrt((t[0]-t[4])**2+(t[1]-t[5])**2)
    bc=math.sqrt((t[2]-t[4])**2+(t[3]-t[5])**2)
    wyn=round(ab+ac+bc,2)
    return wyn

wsp=[]
with open('wspolrzedneTR.txt') as file:
    for line in file:
        czyst=line.rstrip().split()
        wsp.append(czyst)

for line in wsp:
    for i in range(len(line)):
        line[i]=int(line[i])

maxobw=0
wspmax=[]
for line in wsp:
    if obw(line)>maxobw:
        maxobw=obw(line)
        wspmax=line

print(wspmax)
print(maxobw)