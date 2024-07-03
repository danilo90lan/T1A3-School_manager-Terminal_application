import json
from operator import itemgetter
from models import Person, Teacher, Student

# constant
filepath = "./data/school_manager.json"

# function to read from Jason file
def read_json():
    """
    Load students and teachers records from a json file.
    If the file doesn't exist it will be created
    return: List of students, list of teachers and list of the IDs of each record
    if the file is empty or doesn't exists return empty lists
    """
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
            
                if i["Profile"] == Student.profile:
                    # Retrieve the ID for each dictionary in the JSON file and set it to the class variable.
                    # Subtract 1 because creating an instance of the class automatically increments the __id variable by 1,
                    # ensuring that each dictionary keeps its original ID.
                    Person.set_id(i["#ID"] - 1)
                    # create an instance of Student and append it to student list
                    student = Student(i["Name"], i["Last name"], i["Address"], i["Course"])
                    students.append(student)

                elif i["Profile"] == Teacher.profile:
                    Person.set_id(i["#ID"] - 1)
                    # create an instance of Teacher and append it to teacher list
                    teacher = Teacher(i["Name"], i["Last name"], i["Address"], i["Subject"])
                    teachers.append(teacher)    
    except FileNotFoundError:
        with open(filepath, "w") as file:
            json.dump([], file, indent = 4)
    except Exception as error:
        print(f"AN expected error occured: {error}")
    
    return students, teachers, list_id

# function to write on a json file
def write_json(json_data, message="", file_path = filepath):
    """
    Sort a list of a dictionaries in alphabetic order using the sorted function
    and it write it into a json file
    parameters: json_data: list of dictionaries, message: a final message to show after the writing operation,
    it's set as an empty string by default, file_path: path to the json file set to a default value (constant file_path)
    """
    # sort the list in alphabetic order
    sorted_json_data = sorted(json_data, key=itemgetter("Name", "Last name"))
    try:
        with open(file_path, "w") as file:
            json.dump(sorted_json_data, file, indent = 4)
        print(message)
    except PermissionError:
        print("Permission denied to write")
    except Exception as error:
        print(f"AN expected error occured: {error}")
