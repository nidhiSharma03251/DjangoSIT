# move all 0s to end.
list = [0,1,0,4,12,0,5]

for i in list:
    if i==0:
        list.remove(i)
        list.append(i)


print(list)  