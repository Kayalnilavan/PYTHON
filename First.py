id=1001
name="Kayal"
age=22

print("My id is",id)
print("My name is",name)
print("My age is",age)
print("")
print("My id is",id, "\nMy name is",name,"\nMy age is",age)
print("")
output=f"My name is {name}\nMy id is {id}\nMy age is {age}"
print(output)
print("")
output="My name is {}\nMy id is {}\nMy age is {}".format(name,id,age)
print(output)
print("")
output="My name is {0}\nMy id is {1}\nMy age is {2}".format(name,id,age)
print(output)
print("")
output="My name is {1}\nMy id is {0}\nMy age is {2}".format(id,name,age)
print(output)
print("")
print("My name is %s \nMy id is %d\nMy age is %d"%(name,id,age))
