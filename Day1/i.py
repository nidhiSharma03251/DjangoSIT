# to remove duplicate elements while preserving there 1st occurence order. don't use set function.

list=[1,3,4,6,1,3,7,8,9,1]
result = []

for i in list:
    if i not in result:
        result.append(i)
    
print(result)