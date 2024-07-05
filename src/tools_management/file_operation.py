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
    if the file is empty or doesn't exist, return empty lists
    """
    json_data = []      # Stores the JSON data from the file
    students = []       # List to store student objects
    teachers = []       # List to store teacher objects
    list_id = []        # List to store IDs of each record
# read the json file and create new instances of Student and Teacher and put them in two different lists
    try:
        # open file in reading mode
        with open(filepath, "r") as file:
            json_data = json.load(file)
            for i in json_data:
                # Collect IDs from JSON data and append it to the list_id
                list_id.append(i["#ID"])
            
                if i["Profile"] == Student.profile:
                    # Retrieve the ID for each dictionary in the JSON file and set it to the Person class variable.
                    # Subtract 1 because creating an instance of the class automatically increments the __id variable by 1,
                    # in this way each dictionary keeps its original ID.

                    Person.set_id(i["#ID"] - 1)
                    # create an instance of Student using the dictionary keys values as attributes.
                    #  and append it to student list
                    student = Student(i["Name"], i["Last name"], i["Address"], i["Course"])
                    students.append(student)

                elif i["Profile"] == Teacher.profile:
                    Person.set_id(i["#ID"] - 1)
                    # create an instance of Teacher using the dictionary keys values as attributes.
                    # and append it to teacher list
                    teacher = Teacher(i["Name"], i["Last name"], i["Address"], i["Subject"])
                    teachers.append(teacher) 

    except FileNotFoundError:
        # If the file doesn't exist, create an empty JSON file
        with open(filepath, "w") as file:
            json.dump([], file, indent = 4)
    except Exception as error:
        print(f"An expected error occured: {error}")
    
    return students, teachers, list_id

# function to write on a json file
def write_json(json_data, message="", file_path = filepath):
    """
    Sort a list of a dictionaries in alphabetic order using the sorted function that
    returns a new sorted list based on the keys provided, and it write it into a json file
    
    parameters: json_data: list of dictionaries, message (optional): a final message to show after the writing operation,
    it's set as an empty string by default, file_path (optional): path to the json file set to a default value (constant file_path)
    
    return: None
    """
    # sort the list in alphabetic order
    # the sorted function's key parameter is the itemgetter function from the operator module that extracts the value
    # from the "name" and the "last name" keys from a dictionary
    sorted_json_data = sorted(json_data, key=itemgetter("Name", "Last name"))
    try:
        # Open the file in write mode and write the sorted JSON data
        with open(file_path, "w") as file:
            json.dump(sorted_json_data, file, indent = 4)
        # Print the message after successful writing
        print(message)
    except PermissionError:
        print("Permission denied to write")
    except Exception as error:
        print(f"An expected error occured: {error}")
