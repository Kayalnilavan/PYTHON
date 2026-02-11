id = 3000
name="Seelan"
grade="10A"
nic=200130267010

print("---------------------")
print("Student Information")
print("---------------------")
print("Student ID :",id)
print("Student Name :",name)
print("Grade Name :",grade)
print("NIC No:",nic)
print("---------------------")
print(" ")

print("---------------------\nStudent Information\n---------------------\nStudent ID : "+str(id)+"\nStudent Name : "+ name+"\nGrade Name : "+grade+"\nNIC No : "+str(nic)+"\n---------------------")
print(" ")

print(f"---------------------\nStudent Information\n---------------------\nStudent ID :{id}\nStudent Name :{name}\nGrade Name :{grade}\nNIC No :{nic}\n---------------------")
print(" ")

print("---------------------\nStudent Information\n---------------------\nStudent ID :{}\nStudent Name :{}\nGrade Name :{}\nNIC No :{}\n---------------------".format(id,name,grade,nic))
print(" ")

print("---------------------\nStudent Information\n---------------------\nStudent ID :%d \nStudent Name : %s \nGrade Name : %s \nNIC No : %d \n---------------------"%(id,name,grade,nic))