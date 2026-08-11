min=0
max=0
list=[1,3,4,6,1,3,7,8,9,1]

for i in list:
    if i > max:
        max=i
    if i < min:
        min=i

print(f"MIN: ", min)
print(f"MAX: ", max)