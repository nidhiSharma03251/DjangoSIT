# wap that accepts a tuple of integers and returns a new tuple containing:
# duplicate els
# unique els
# 2nd largest and snd smallest
# frequency of all els

t=(1,3,4,6,1,3,7,8,9,1)
duplicate=[]
unique=[]
d={}

list=set(t)
list=sorted(list)

print(f"Second largest: ",list[-2])
print(f"Second smallest: ",list[1])

for i in t:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1

for i in d.keys():
    if d[i]==1:
        unique.append(i)
    else:
        duplicate.append(i)

print(tuple(unique))
print(tuple(duplicate))

print(d)

