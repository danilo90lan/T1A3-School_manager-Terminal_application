import json

class Person:
    # class variable
    # encapsulation
    __id = 1

    def __init__(self, name, last_name, address):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.id = Person.__id
        Person.__id += 1

    def get_ID(self):
        return self.id

    def print_info(self):
        info = f"""
        #ID: {self.id}
        Name: {self.name}
        Last name: {self.last_name}
        Address: {self.address}"""
        return info 
    
    def update_info(self):
        print(f"""Update info: 
              1 - Name
              2 - Last Name
              3 - Address
              """)
        choice = int(input("What would you like to update? "))

        match choice:
            case 1:
                self.name = input("New name --> ")
            case 2:
                self.last_name = input("New last name --> ")
            case 3:
                self.address = input("New address --> ")
            case _:
                print("Invalid choice. Input must be between 1 and 3")

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

    def __init__(self, name, last_name, address, subject_area = []):
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
    new_record = {  "#ID": student.get_ID(),
                    "Name": student.name,
                    "LastName": student.last_name,
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
    new_record = {  "#ID": teacher.get_ID(),
                    "Name": teacher.name,
                    "LastName": teacher.last_name,
                    "Address": teacher.address,
                    "Teaching Subjects": teacher.subject_area,
                    "Profile": teacher.profile}
    return new_record

# writing to a Jason file
# def write_json(record):
#     filename = "./data/uni_database.json"
#     data = []
#     try:
#         with open(filename, "r") as file:
#             data = json.load(file)
#     except FileNotFoundError:
#             print(f"File not found. Creating a a new file...")
#     except json.JSONDecodeError:
#             #if the file exists but contains invalid JSON, raise an error
#             print("Error decoding JSON from the file")
#     data.append(record)

#     with open(filename, "w") as file:
#         json.dump(data, file, indent = 3)
#     print("Data added succesfully!")

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
    file_data = []
    try:
        with open(filepath, "r") as file:
            file_data = json.load(file)
            return file_data
    except FileNotFoundError:
        with open(filepath, "w") as file:
            json.dump([], file, indent = 4)

def main():

    student_list = []
    teacher_list = []

    while True:
        choice = input_menu()

        match choice:
            case "1":
                teacher_list.append(teacher_new_record())
                new_record = "Y"
                while new_record not in ("Nn"):
                    new_record = input("Do you want to enter another one? (Y/N) ")
                    if new_record in ("Yy"):
                        teacher_list.append(teacher_new_record())
                # write_json(teacher_list)
                print(teacher_list)

            case "2":
                student_list.append(student_new_record())
                new_record = "Y"
                while new_record not in ("Nn"):
                    new_record = input("Do you want to enter another one? (Y/N) ")
                    if new_record in ("Yy"):
                        student_list.append(student_new_record())
                # write_json(student_list)
                print(student_list)

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

main()