print("a. Non century leap year ")
print("b. Century leap year ")
print("c. Non century non-leap year ")
print("d. Century non-leap year ")
ch=int(input("Enter year -> "))
match  ch%100==0:
    case 1:
        print("century leap year") if ch%400==0 else print("Century non-leap year")
    case 0:
        print("non Century leap year") if ch%4==0 else print("non Century non leap year ")

        
        
