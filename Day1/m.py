list=[1,-3,4,6,-1,3,7,8,-9,1]

for i in range(len(list)):
    if list[i] < 0:
        list[i]=0

print(list)