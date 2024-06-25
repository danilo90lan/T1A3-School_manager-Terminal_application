import json

class Person:

    def __init__(self, name, last_name, address):
        self.name = name
        self.last_name = last_name
        self.address = address

    def print_info(self):
        info = f"""
        Name: {self.name}
        Last name: {self.last_name}
        Address: {self.address}"""
        return info 
    
    def update_info(self):
        print(f"""Update info: 
              1 - Name
              2 - Last Name
              3 - Address
              4 - Cancel operation
              """)
        while True:
            choice = input("What would you like to update? ")

            match choice:
                case "1":
                    self.name = input("New name --> ")
                case "2":
                    self.last_name = input("New last name --> ")
                case "3":
                    self.address = input("New address --> ")
                case "4":
                    print("Update operation cancelled")
                case _:
                    print("Invalid choice. Try again")

class Student(Person):
    # class variable
    profile = "Student"

    def __init__(self, name, last_name, address, course):
        super().__init__(name, last_name, address)
        self.course = course

    def print_info(self):
        info = f"""
        Profile: {Student.profile}
        Course name: {self.course}
        """
        return super().print_info() + info
    
    def update_course(self,new_course):
        self.course = new_course
        print("Course Updated")
    
class Teacher(Person):
    # class variable
    profile = "Teacher"

    def __init__(self, name, last_name, address, subject_area = [],):
        super().__init__(name, last_name, address)
        self.subject_area = subject_area

    def print_info(self):
        info = f"""
        Profile: {Teacher.profile}
        Teaching area: {self.subject_area}
        """
        return super().print_info() + info
    
    def update_subjects(self, new_subjects):
                new_list = []
                for i in new_subjects:
                    new_list.append(i)
                self.subject_area = new_list
                print(f"Subjects added")

def student_new_record():
    name = input("Enter name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    course = input("Enter course name: ")
    student = Student(name, last_name, address, course)
    new_record = {  "Name": student.name,
                    "Last Name": student.last_name,
                    "Address": student.address,
                    "Course": student.course,
                    "Profile": student.profile}
    return new_record

def teacher_new_record():
    name = input("Enter name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    course = input("Enter teaching subjects (separate each subject with a space): ").split()
    teacher = Teacher(name, last_name, address, course)
    new_record = {  "Name": teacher.name,
                    "LastName": teacher.last_name,
                    "Address": teacher.address,
                    "Teaching Subjects": teacher.subject_area,
                    "Profile": teacher.profile}
    return new_record

# defining menu function
def input_menu():
    print(f"""
    1 - Insert new teacher
    2 - Insert new student
    3 - Visualize students records
    4 - Visualize teachers records
    5 - Update students info
    6 - Update teachers info
    7 - Exit program
    """)
    return input("Enter your choice: ")

# function to read from Jason file
def read_json():
    filepath = "./data/uni_database.json"
    json_data = []
    students_instances= []
    teachers_instances = []

    try:
        with open(filepath, "r") as file:
            json_data = json.load(file)
                
    except FileNotFoundError:
        with open(filepath, "w") as file:
            json.dump([], file, indent = 4)
    return teachers_instances, students_instances

# function to write on a json file
def write_json(json_data):
    filepath = "./data/uni_database.json"
    
    with open(filepath, "w") as file:
        json.dump(json_data, file, indent = 4)
    print("Data added succesfully")



def main(): 
    

    while True:
        choice = input_menu()

        match choice:
            case "1":
                records_list.append(teacher_new_record())
                new_record = "Y"
                while new_record not in ("Nn"):
                    new_record = input("Do you want to enter another one? (Y/N) ")
                    if new_record in ("Yy"):
                        records_list.append(teacher_new_record())
                write_json(records_list)

            case "2":
                records_list.append(student_new_record())
                new_record = "Y"
                while new_record not in ("Nn"):
                    new_record = input("Do you want to enter another one? (Y/N) ")
                    if new_record in ("Yy"):
                        records_list.append(student_new_record())
                write_json(records_list)

            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                print("Program ended.")
                break
            case _:
                print("Input not valid. Try again")

records_list = []

json_data = read_json()

main()