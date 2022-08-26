x=str(input("enter your favourite color "))
print(x)
if "yello" in x:
    ch='a'
elif "blue" in x:
    ch='b'
elif "orange" in x:
    ch='c'
elif "white" in x:
    ch='d'
elif "black" in x:
    ch='e'
elif "red" in x:
    ch='f'
else:
    ch='g'
match ch:
    case 'a':
        print("Yellow - Monday")
    case 'b':
        print("Blue - Tuesday")
    case 'c':
        print("Orange - Wednesday")
    case 'd':
        print("White - Thursday")
    case 'e':
        print("Black - Friday")
    case 'f':
        print("red - Saturday ")
    case 'g':
        print("Sunday ")
    
