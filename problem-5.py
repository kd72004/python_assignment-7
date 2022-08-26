x=int(input("Enter a number "))
if x%2==0:
    ch=1
else:
    if(x<0):
        ch=2
    else:
        ch=3
match ch:
    case 1:
        print("Saurabh Shukla")
    case 2:
        print("Prateek Jain")
    case 3:
        print("Aditya Choudhary")
