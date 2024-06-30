import json
from operator import itemgetter
from converting_type import studentObject_to_Dict, teacherObject_to_Dict

# function to read from Jason file
def read_json():
    from models import Person
    from models import Teacher
    from models import Student

    filepath = "./data/school.json"
    json_data = []
    students = []
    teachers = []
    list_id = []
# read the json file and create new instances of Student and Teacher and put them in two different lists
    try:
        with open(filepath, "r") as file:
            json_data = json.load(file)
            for i in json_data:
                list_id.append(i["#ID"])
            
                if i["Profile"] == "Student":
                    #get the id for each dictionary in the json file and set it in the variable class -1
                    # because when the class instance is created automatically increase the __id variable by 1
                    # so in this way each dictionary keeps the original id
                    Person.set_id(i["#ID"] - 1)
                    # create an instance of Student and append it to student list
                    student = Student(i["Name"], i["Last name"], i["Address"], i["Course"])
                    students.append(student)

                elif i["Profile"] == "Teacher":
                    Person.set_id(i["#ID"] - 1)
                    # create an instance of Teacher and append it to teacher list
                    teacher = Teacher(i["Name"], i["Last name"], i["Address"], i["Subject"])
                    teachers.append(teacher)
            
    except FileNotFoundError:
        with open(filepath, "w") as file:
            json.dump([], file, indent = 4)

    return students, teachers, list_id

# function to write on a json file
def write_json(json_data, message="", file_path = "./data/school.json"):
    # sort the list in alphabetic order
    sorted_json_data = sorted(json_data, key=itemgetter("Name", "Last name"))

    with open(file_path, "w") as file:
        json.dump(sorted_json_data, file, indent = 4)
    print(message)
