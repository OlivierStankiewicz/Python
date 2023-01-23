def ktora_cw(t):
    x,y,r = float(t[0]), float(t[1]), float(t[2])
    if x>0 and y>0 and x-r>0 and y-r>0:
        return 1
    elif x<0 and x+r<0 and y>0 and y-r>0:
        return 2
    elif x<0 and x+r<0 and y<0 and y+r<0:
        return 3
    elif x>0 and x-r>0 and y<0 and y+r<0:
        return 4
    else:
        return 0



okregi=[]
with open('okregi.txt') as file:
    for line in file:
        czyst=line.rstrip().split()
        okregi.append(czyst)

I=0
II=0
III=0
IV=0
inne=0

for item in okregi:
    if ktora_cw(item) == 1:
        I+=1
    elif ktora_cw(item) == 2:
        II+=1
    elif ktora_cw(item) == 3:
        III+=1
    elif ktora_cw(item) == 4:
        IV+=1
    elif ktora_cw(item) == 0:
        inne+=1

print(I)
print(II)
print(III)
print(IV)
print(inne)