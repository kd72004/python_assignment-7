num =int(input("Input a number: "))
match num>0:
    case 1:
        print("you entered positive ")
    case 0:
        print("you entered zero") if num==0 else print("you entered negative")
