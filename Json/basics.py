import json

student1 = {
    "Id" : 1,
    "First Name" : "Rifat",
    "Last Name" : "Miah",
    "Email" : "riaft@gmail.com",
    "Age" : 23,
    "Gender" : "Male",
    "Date of Birth " :  "28 January, 2003"
}

student2 = {
    "Id" : 2,
    "First Name" : "Rony",
    "Last Name" : "Khan",
    "Email" : "ronyt@gmail.com",
    "Age" : 33,
    "Gender" : "Male",
    "Date of Birth " :  "16 June, 2003"
}

student_list = [student1, student2]

with open("students.json", "w") as f:     # open(new_destination_file_name, r{read} / w {write})
    json.dump(student_list, f, indent= 4)  
    
    '''
    json.dump : function which directly writes the dictionary to a file in the form of JSON, without needing to convert it into an actual JSON object.
    
    It takes 2 parameters:
    a) dictionary - the name of a dictionary which should be converted to a JSON object.
    b) file pointer - pointer of the file opened in write or append mode.
    '''
    # indent: defines the number of units for indentation