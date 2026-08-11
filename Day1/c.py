list=[12,22,34,56,11,89]
lar=0
sL = 0

for i in list:
    if i > lar:
        lar=i

for i in list:
    if i!=lar and i>sL:
        sL=i

print(sL)