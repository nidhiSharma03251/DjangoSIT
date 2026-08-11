# WAP for an ATM machine that accepts a withdrawal amount and checks:
# amount must be a multiple of 100
# amount must not exceed the main bal
# minimum bal after withdrawal must be 500
# otherwise print a msg

balAmt = 50000
withdrawAmt = int(input("Enter withdrawal amount: "))
remaining = balAmt-withdrawAmt

if withdrawAmt%100 == 0:
    if remaining < 500:
        print("Amount Cannot be withdrawn")
    elif withdrawAmt > balAmt:
        print("Amount Cannot be withdrawn")
    else:
        print("Amount Cann be withdrawn")
        print(remaining)
else:
    print("Amount Cannot be withdrawn")


