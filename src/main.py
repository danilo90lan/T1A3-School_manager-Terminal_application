import json

class Person:
    #class variable
    __id = 1

    def __init__(self, name, last_name, address):
        self.id = Person.__id
        self.name = name
        self.last_name = last_name
        self.address = address
        Person.__id += 1

    def getID():
        return Person.__id
    
    def setID(new_id):
        Person.__id = new_id

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
    # class const
    profile = "Student"

    def __init__(self, name, last_name, address, course):
        super().__init__(name, last_name, address)
        self.course = course
        self.profile = Student.profile

    def print_info(self):
        info = f"""
        Profile: {self .profile}
        Course name: {self.course}
        """
        return super().print_info() + info
    
    def update_course(self,new_course):
        self.course = new_course
        print("Course Updated")

class Teacher(Person):
    # class const
    profile = "Teacher"

    def __init__(self, name, last_name, address, subject_area = [],):
        super().__init__(name, last_name, address)
        self.subject_area = subject_area
        self.profile = Teacher.profile

    def print_info(self):
        info = f"""
        Profile: {self.profile}
        Teaching area: {self.subject_area}
        """
        return super().print_info() + info
    
    def update_subjects(self, new_subjects):
                new_list = []
                for i in new_subjects:
                    new_list.append(i)
                self.subject_area = new_list
                print(f"Subjects added")

# converting to dictionary
def studentObject_to_Dict(student_instance):
    new_dict = {"#ID": Person.getID(),
                "Name": student_instance.name,
                "Last name": student_instance.last_name,
                "Address": student_instance.address,
                "Course": student_instance.course,
                "Profile": student_instance.profile
    }
    return new_dict

def teacherObject_to_Dict(teach_instance):
    new_dict = { "#ID": Person.getID(),
                "Name": teach_instance.name,
                "Last name": teach_instance.last_name,
                "Address": teach_instance.address,
                "Teaching subjects": teach_instance.subject_area,
                "Profile": teach_instance.profile
    }
    return new_dict

def student_new_record():
    name = input("Enter name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    course = input("Enter course name: ")
    student = Student(name, last_name, address, course)
    students_instances.append(student)
    new_record = studentObject_to_Dict(student)
    return new_record

def teacher_new_record():
    name = input("Enter name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    course = input("Enter teaching subjects (separate each subject with a space): ").split()
    teacher = Teacher(name, last_name, address, course)
    teachers_istance.append(teacher)
    new_record = teacherObject_to_Dict(teacher)
    return new_record

# defining menu function
def input_menu():
    print(f"""
    1 - Enter new teacher
    2 - Enter new student
    3 - Visualize students records
    4 - Visualize teachers records
    5 - Search student
    6 - Search teacher
    7 - Update students info
    8 - Update teachers info
    9 - Exit program
    """)
    return input("Enter your choice: ")

# function to read from Jason file
def read_json():
    filepath = "./data/uni_database.json"
    json_data = []
    students = []
    teachers = []
    id_list = []

    try:
        with open(filepath, "r") as file:
            json_data = json.load(file)
            for i in json_data:
                id_list.append(i["#ID"])
                if i["Profile"] == "Student":
                    student = Student(i["Name"], i["Last name"], i["Address"], i["Course"])
                    students.append(student)
                elif i["Profile"] == "Teacher":
                    teacher = Teacher(i["Name"], i["Last name"], i["Address"], i["Teaching subjects"])
                    teachers.append(teacher)
            
    except FileNotFoundError:
        with open(filepath, "w") as file:
            json.dump([], file, indent = 4)
    return students, teachers, id_list

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
                new_list.append(teacher_new_record())
                new_record = "Y"
                while new_record not in ("Nn"):
                    new_record = input("Do you want to enter another one? (Y/N) ")
                    if new_record in ("Yy"):
                        new_list.append(teacher_new_record())
                write_json(new_list)

            case "2":
                new_list.append(student_new_record())
                new_record = "Y"
                while new_record not in ("Nn"):
                    new_record = input("Do you want to enter another one? (Y/N) ")
                    if new_record in ("Yy"):
                        new_list.append(student_new_record())
                write_json(new_list)

            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "9":
                print("Program ended.")
                break
            case _:
                print("Input not valid. Try again")

# for i in students_instances:
#     print(i.name)
#     print(i.profile)


# for i in teachers_istance:
#     info = Teacher.print_info(i)
#     print(info)


    
new_list = []
students_instances, teachers_istance, json_id = read_json()
for i in students_instances:
        new_list.append(studentObject_to_Dict(i))

for i in teachers_istance:
        new_list.append(teacherObject_to_Dict(i))

# seeting a new __id value
Person.setID(max(json_id))

main()