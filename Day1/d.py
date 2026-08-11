# Check if date is valid

date = "26/04/2004"

data = date.split("/")
flag=0

data[1] = int(data[1])
if data[1]>=1 and data[1]<=12:
    flag=1
else:
    return "Not a valid date"

# Check no. of days in a month
if data[1]<=7 and data[1]%2==0 :
    month = 30
else:
    month = 31

if data[1]>=7 and data[1]%2==0:
    month = 30
else:
    month = 31

# Check date
if month == 30:
data[0] = int(data[0])

if data[0]>=1 and data[0]<=30:
    flag=1
else:
    return "Not a valid date"


if month == 31:

if data[0]>=1 and data[0]<=31:
    flag=1
else:
    return "Not a valid date"




