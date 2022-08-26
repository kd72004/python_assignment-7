print("a. Check whether a given set of three numbers are lengths of an isosceles triangle or ")
print("b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not")
print("c. Check whether a given set of three numbers are equilateral triangle or not -> ")
print("d. exit ")
ch=str(input("enter your choice -> "))
a=int(input("enter first length of triangle -> "))
b=int(input("enter second length of triangle -> "))
c=int(input("enter third length of triangle -> "))
match ch:
    case "a":
        if(a==b && b==c && a==c):
            print("it is an isosceles triangle ")
        else:
            print("it is not an isosceles triangle ")
    case "b":
        print("yes")
    case "c":
        if(a==b && b==c):
            print("Equilateral Triangle ")
        else:
            print("not an Equilateral Triangle ")
    case "d":
        exit(0)
