print("1.Monday\n2.Tuesday\n3.Wednesday\n4.Thursday\n5.Friday\n6.Saturday\n7.Sunday")
day=int(input("Day :"))
match day:
    case 1 :
        print("Day : Monday")
    case 2 :
        print("Day : Tuesday")
    case 3 :
        print("Day : Wednesday")
    case 4 :
        print("Day : Thursday")
    case 5 :
        print("Day : Friday")
    case 6 :
        print("Day : Saturday")
    case 7 :
        print("Day : Sunday")
    case _ :
        print("Invalid Number")