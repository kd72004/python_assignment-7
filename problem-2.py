print("1. addition ")
print("2.subtraction")
print("3. multiplication")
print("4. division")
x=int(input("enter your choice ->"))
y=int(input("enter a number -> "))
z=int(input("enter a number -> "))
match x:
    case 1:
        print(z+y)
    case 2:
        print(y-z)
    case 3:
        print(z*y)
    case 4:
        print(y/z)

        
