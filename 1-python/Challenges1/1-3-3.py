#rite a program to read in a string of students and gpas in one input statement like this:

#`tom 3.4, noel 3.2, obby 3.5, peta 3.4`

#nd write out JSON like this:

#```
#[
#    { "name" : "tom", "gpa" : 3.4 },
#    { "name" : "noel", "gpa" : 3.2 },
#    { "name" : "obby", "gpa" : 3.5 },
#    { "name" : "peta", "gpa" : 3.4 }
#]
#```

#Suggested approach:

#    1. input text
#    2. for each student split on "," from the text
#    3.    split the student into name and gpa 
#    4.    parse the gpa so its a float
#    5.    add the name and gpa to the list
#    6. write the list to students.json as JSON

import json

folder_name = "1-python/data"
text = input("Enter students and gpas: ")
students_list = []
students = text.split(",")

for student in students:
    name_gpa = student.strip().split(" ")
    name = name_gpa[0]
    gpa = float(name_gpa[1])
    students_list.append({"name": name, "gpa": gpa})
with open("students.json", "w") as f:
    json.dump(students_list, f, indent=4)
    

