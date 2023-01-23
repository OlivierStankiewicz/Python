napisy=[]
with open('napisy.txt') as file:
    for line in file:
        czyst=line.rstrip().split()
        napisy.append(czyst)

for line in napisy:
    if line[0] == line[1][:len(line[0])]:
        print(line)
        print(line[1][len(line[0]):])