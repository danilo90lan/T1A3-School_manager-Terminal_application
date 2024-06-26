import json

class Person:
    #class variable
    __id = 0

    def __init__(self, name, last_name, address):
        Person.__id += 1
        self.name = name
        self.last_name = last_name
        self.address = address
        
    @classmethod
    def get_id(cls):
        return Person.__id
    
    @classmethod
    def set_id(cls, new_id):
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
        self.__id = Person.get_id()

    def get_id(self):
        return self.__id

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
        self.__id = Person.get_id()

    def get_id(self):
        return self.__id

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

class School:
    def __init__(self, students, teachers):
        self.students = students
        self.teachers = teachers
    
    def print_all_students(self):     
        for i in self.students:
            print(Student.print_info(i))

    def print_all_teachers(self):     
        for i in self.teachers:
            print(Teacher.print_info(i))


# converting to dictionary
def studentObject_to_Dict(student_instance):
    new_dict = {"#ID": student_instance.get_id(),
                "Name": student_instance.name,
                "Last name": student_instance.last_name,
                "Address": student_instance.address,
                "Course": student_instance.course,
                "Profile": student_instance.profile
    }
    return new_dict

def teacherObject_to_Dict(teach_instance):
    new_dict = { "#ID": teach_instance.get_id(),
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
    return student

def teacher_new_record():
    name = input("Enter name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    course = input("Enter teaching subjects (separate each subject with a space): ").split()
    teacher = Teacher(name, last_name, address, course)
    return teacher

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
    list_id = []
# read the json file and create new instances of Student and Teacher and put them in two different lists
    try:
        with open(filepath, "r") as file:
            json_data = json.load(file)
            for i in json_data:
                list_id.append(i["#ID"])
            
                if i["Profile"] == "Student":
                    Person.set_id(i["#ID"])
                    student = Student(i["Name"], i["Last name"], i["Address"], i["Course"])
                    students.append(student)
                elif i["Profile"] == "Teacher":
                    Person.set_id(i["#ID"])
                    teacher = Teacher(i["Name"], i["Last name"], i["Address"], i["Teaching subjects"])
                    teachers.append(teacher)
            
    except FileNotFoundError:
        with open(filepath, "w") as file:
            json.dump([], file, indent = 4)

    return students, teachers, list_id

# function to write on a json file
def write_json(json_data):
    filepath = "./data/uni_database.json"
    
    with open(filepath, "w") as file:
        json.dump(json_data, file, indent = 4)
    print("Data added succesfully")



def main(): 

    #Initializzation
    # contains a list of students and teachers converted into dictionaries, ready to be written in the json file 
    json_file_list = []

    students_instances, teachers_instances, list_id = read_json()

    for i in students_instances:
            json_file_list.append(studentObject_to_Dict(i))

    for i in teachers_instances:
            json_file_list.append(teacherObject_to_Dict(i))
    
    for i in json_file_list:
        print(i["#ID"])
    
    while True:
        choice = input_menu()

        match choice:
            case "1":
                new_record = "Y"
                while new_record in ("Yy"):
                    #instance a new Teacher object
                    new_teacher = teacher_new_record()
                    # update teachers list
                    teachers_instances.append(new_teacher)
                    # append the new object converted into a dictionary to the json list
                    json_file_list.append(teacherObject_to_Dict(new_teacher))
                    new_record = input("Do you want to enter another one? (Y/N) ")
                # write to json file
                for i in json_file_list:
                    print(i["#ID"])
                write_json(json_file_list)
                school = School(students_instances, teachers_instances)

            case "2":
                new_record = "Y"
                while new_record in ("Yy"):
                    #instance a new Student object
                    new_student = student_new_record()
                    # update students_list
                    students_instances.append(new_student)
                    # append the new object converted into a dictionary to the json list
                    json_file_list.append(studentObject_to_Dict(new_student))
                    new_record = input("Do you want to enter another one? (Y/N) ")
                # write to json file
                for i in json_file_list:
                    print(i["#ID"])
                
                write_json(json_file_list)
                school = School(students_instances, teachers_instances)

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

main()