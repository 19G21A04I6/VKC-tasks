
a = int(input("Enter the Account Number :"))
b = int(input("Enter The PIN NO :"))
if a == 1234567890 and b==1234 :
    print("Account details is valid")
    print('''    Enter 1 to withdraw
    Enter 2 to balance enquiry''')
    c=int(input("enter the number :"))
    if c==1:
        d=int(input("enter the amount :"))
        if d>150000:
            print("insuffient balance")
        else:
            c = (150000-d)
            print("Amount Debited")
            print("Balance Amount :",c)
    elif(c==2):
        print(" Balance Amount = 150000")
    else:
        print("Select the Valid Number")
else:
    print("Invalid Account Number / PIN NO :")
