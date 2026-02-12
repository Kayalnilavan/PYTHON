unit=int(input("Units : "))

case1= unit*7
case2= 90*7 + (unit-90)*10
case3= 90*7 + 150*10 + (unit-150)*15
case4= case3 + case3*0.03

if unit>0 and unit<90 :
    print("Bill amount : Rs.",case1)
elif unit<150 :
    print("Bill amount : Rs.",case2)
elif unit<300:
    print("Bill amount : Rs.",case3)
else :
    print("Bill amount : Rs.",case4)