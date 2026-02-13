num1=int(input("Number 1 : "))
num2=int(input("Number 2 : "))
fun=int(input("Select function\n1.Addition\t2.Subtraction\t3.Multiplication\t4.Division\nFunction : "))
match fun:
    case 1:
        num3=num1+num2
        print("Output :",num3)
    case 2:
        num3=num1-num2
        print("Output :",num3)
    case 3:
        num3=num1*num2
        print("Output :",num3)
    case 4:
        if num1==0 and num2==0 :
            print("Output : Undifined")
        elif num2==0:
            print("Output : Infinity")
        else:
            num3=num1/num2
            print("Output :",num3)
    case _:
        print("Invalid function")