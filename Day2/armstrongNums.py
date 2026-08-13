

for i in range(1, 1001):
    sum=0
    temp=i
    while(i != 0):
        ld=i%10
        sum = sum+ ld**3
        i = i//10

    if(sum == temp):
        print(temp)

