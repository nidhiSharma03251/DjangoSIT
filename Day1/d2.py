# Check if date is valid

date = "26/04/2004"

data = date.split("/")

day = int(data[0])
month = int(data[1])
year = int(data[2])

if len(data)>3:
    print("Invalid")
elif year%4==0 and month==2 and day>29:
    print("Invalid")
elif month==2 and day>28:
    print("Invalid")
elif month>12:
    print("invalid")
elif month<=7 and month%2==0 and day>30:
    print("invalid")
elif month>7 and month%2!=0 and day>31:
    print("invalid")
else:
    print("valid") 