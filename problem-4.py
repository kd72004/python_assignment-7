x=int(input("Enter your age -> "))
if x<10:
    ch=10
elif x<20:
    ch=20
elif x<40:
    ch=30
elif x<60:
    ch=50
else:
    ch=60
match ch:
    case 10:
        print("You are a kid ")
    case 20:
        print("You are a teen ")
    case 30:
        print("You are a young ")
    case 50:
        print("You are an Experienced")
    case 60:
        print("You are Senior Citizen")
        
