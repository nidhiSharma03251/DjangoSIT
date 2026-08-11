
list=[1,31,14,16,11,3,7,8,9,1]
sum=0
for i in list:
    sum += i

avg=sum/len(list)
# print(avg)
count=0
for i in list:
    if i > avg:
        count += 1

print(count)