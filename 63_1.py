ciagi=[]
with open('ciagi.txt') as file:
    for line in file:
        czyst=line.rstrip()
        ciagi.append(czyst)

for item in ciagi:
    if len(item)%2==0:
        if item[:len(item)//2] == item[len(item)//2:]:
            print(item)