print("--- Student Dictionary Management ---")
#create student dictionary 
student={
"name":"ketan",
"roll_no":11,
"course":"BA",
"marks":450
}
#printing a dictionary 
print("\nstudent dictionary:",student)
#updating a student marks
student["marks"]=460
print ("\nupdated student dictionary:",student)
#adding a city key in student dictionary 
student ["city"]="pune"
print ("\nstudent city is added:",student)
#removing city key from student dictionary 
student.pop("city")
print("\nremoving city from student:",student)
#length of dictionary 
print("\nlength of student dictionary:",len(student))
#student keys
print ("\nstudent keys:",student.keys())
#student values
print ("\nstudent values:",student.values())
print ("\nstudent dictionary items:")
#student dictionary items
for key,value in student.items():
    print ("\t",key,":",value)