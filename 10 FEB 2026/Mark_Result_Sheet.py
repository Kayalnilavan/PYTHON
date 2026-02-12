mark = int(input("Enter your marks : "))

if mark<=100 and mark>=0 :
    if mark>=75 :
        print("Result : A")
    elif mark>=65 :
        print("Result : B")
    elif mark>=55 :
        print("Result : C")
    elif mark>=45 :
        print("Result : S")
    else :
        print("Result : W")
else:
    print("Incorrect value")