# a list contains n distinct no.s from 0 to n find the missing number without using sum function.
list=[1,3,4,7,8,6,2,5]
actualSum=0
requiredSum=0

for i in list:
    actualSum += i

for i in range(0,10):
    requiredSum += i

print(requiredSum-actualSum)


