import json
from operator import itemgetter

class Person:
    # class variable
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
        ID: {self.get_id()}
        Name: {self.name}
        Last name: {self.last_name}
        Address: {self.address}"""
        return info

    def update_info(self):
        self.name = input("New name --> ").capitalize()
        self.last_name = input("New last name --> ").capitalize()
        self.address = input("New address --> ").capitalize()

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
        Profile: {self.profile}
        Course name: {self.course}
        """
        return super().print_info() + info
    
    def update_student(self):
        super().update_info()
        self.course = input("New course --> ").capitalize()
        print("\nStudent info updated succesfully!")

class Teacher(Person):
    # class const
    profile = "Teacher"

    def __init__(self, name, last_name, address, subject_area):
        super().__init__(name, last_name, address)
        self.subject_area = subject_area
        self.profile = Teacher.profile
        self.__id = Person.get_id()

    def get_id(self):
        return self.__id

    def print_info(self):
        info = f"""
        Profile: {self.profile}
        Teaching subject: {self.subject_area}
        """
        return super().print_info() + info
    
    def update_teacher(self):
            super().update_info()
            self.subject_area = input("New teaching subject --> ").capitalize()
            print("\/Teacher info updated succesfully!")

class School:
    def __init__(self, students, teachers):
        self.students = students
        self.teachers = teachers

    def display_all_students(self):
        if self.students != []: 
            # sort alphabetically
            sorted_students = sorted(self.students, key=lambda student: (student.name, student.last_name))
            for i in sorted_students:
                print(Student.print_info(i))
        else:
            print("\nThere is no students records")

    def display_all_teachers(self):
        if self.teachers != []: 
            # sort alphabetically
            sorted_teachers = sorted(self.teachers, key=lambda teacher: (teacher.name, teacher.last_name))
            for i in sorted_teachers:
                print(Teacher.print_info(i))
        else:
            print("\nThere is no teachers records")

    def find_student_by_id(self, student_id):
        found =False

        for i in self.students:
            if Student.get_id(i) == student_id:
                record = i
                found = True
                break
        try:
            print(Student.print_info(record))
        except UnboundLocalError:
            print("\nStudent record NOT in the system")
        return found
    
    def find_student_by_name(self, student_name):
        record = False

        for i in self.students:
            if i.name.lower() == student_name.lower():
                print(Student.print_info(i))
                record = True
        if record == False:
            print("\nStudent recond NOT in the system")
        return record

    def find_teacher_by_id(self, teacher_id):
        found = False

        for i in self.teachers:
            if Teacher.get_id(i) == teacher_id:
                record = i
                found = True
                break
        try:
            print(Teacher.print_info(record))
        except UnboundLocalError:
            print("\nTeacher record NOT in the system")
        return found
    
    def find_teacher_by_name(self, teacher_name):
        record = False

        for i in self.teachers:
            if i.name.lower() == teacher_name.lower():
                print(Teacher.print_info(i))
                record = True
        if record == False:
            print("\nTeacher recond NOT in the system")
        return record

    def student_update(self, id):
        for i in self.students:
            if Student.get_id(i) == id:
                Student.update_student(i)
        write_json(self.students, self.teachers)

    def teacher_update(self, id):
        for i in self.teachers:
            if Teacher.get_id(i) == id:
                Teacher.update_teacher(i)   
        write_json(self.students, self.teachers)

    def filter_students_by_course(self, course):
        for i in self.students:
            if i.course.lower() == course.lower():
                print(Student.print_info(i))
    
    def filter_teachers_by_subject(self, subject):
        for i in self.teachers:
            if i.subject_area.lower() == subject.lower():
                print(Teacher.print_info(i))

def student_new_record():
    name = input("Enter name: ").capitalize()
    last_name = input("Enter last name: ").capitalize()
    address = input("Enter address: ").capitalize()
    course = input("Enter course name: ").capitalize()
    student = Student(name, last_name, address, course)
    return student

def teacher_new_record():
    name = input("Enter name: ").capitalize()
    last_name = input("Enter last name: ").capitalize()
    address = input("Enter address: ").capitalize()
    course = input("Enter teaching subject: ").capitalize()
    teacher = Teacher(name, last_name, address, course)
    return teacher

# defining menu function
def input_menu():
    print(f"""
    1 - Enter new teacher
    2 - Enter new student
    3 - Display teachers records (A - Z)
    4 - Display students records (A - Z)
    5 - Search student
    6 - Search teacher
    7 - Filter teachers by teaching subject
    8 - Filter students by course
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

# converting students to dictionary
def studentObject_to_Dict(students):
    list_students = []
    for i in students:
        student_dict = {"#ID": i.get_id(),
                    "Name": i.name,
                    "Last name": i.last_name,
                    "Address": i.address,
                    "Course": i.course,
                    "Profile": i.profile
                    }
        list_students.append(student_dict)
    return list_students

# converting teachers instances to dictionary
def teacherObject_to_Dict(teachers):
    list_teachers = []
    for i in teachers:
        teacher_dict = { "#ID": i.get_id(),
                    "Name": i.name,
                    "Last name": i.last_name,
                    "Address": i.address,
                    "Subject": i.subject_area,
                    "Profile": i.profile
        }
        list_teachers.append(teacher_dict)
    return list_teachers

# function to write on a json file
def write_json(students_objects, teachers_objects):
    json_data = studentObject_to_Dict(students_objects) + teacherObject_to_Dict(teachers_objects)
    # sort the list in alphabetic order
    sorted_json_data = sorted(json_data, key=itemgetter("Name", "Last name"))
    filepath = "./data/uni_database.json"
    
    with open(filepath, "w") as file:
        json.dump(sorted_json_data, file, indent = 4)
    print("Data added successfully")

def menu2(record, id = None):
    print("What would you like to do?")                       
    while True:
        print(f"""
        1 - Update info
        2 - Delete record
        3 - Back 
        """)
        scelta = input("Enter your operation: ")
        match scelta:
            case "1":
                if id == None:
                    id = int(input("Enter ID to confirm the correct record to update in case there are homonyms: "))
                if record == "student":
                    school.student_update(id)
                    break
                elif record == "teacher":
                    school.teacher_update(id)
            case "2":
                if id == None:
                    id = int(input("Enter ID to delete: "))
                pass
            case "3":
                break
            case _:
                print("Invalid input. Try again")

# Initializzation
students_instances, teachers_instances, list_id = read_json()
#create school instance with 2 arguments student_list and teachers_list
school = School(students_instances, teachers_instances)
# set the ID to the highest number in order for each element of the list to have a unique ID
Person.set_id(max(list_id))

# main function
def main(): 

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
                    new_record = input("\nDo you want to enter another one? (Y/N) ")
                    print("\n")
                # write to json file after adding all new records
                write_json(students_instances, teachers_instances)

            case "2":
                new_record = "Y"
                while new_record in ("Yy"):
                    #instance a new Student object
                    new_student = student_new_record()
                    # update students list
                    students_instances.append(new_student)
                    new_record = input("\nDo you want to enter another one? (Y/N) ")
                    print("\n")
                # write to json file after adding all new records
                write_json(students_instances, teachers_instances)

            case "3":
                school.display_all_teachers()
            case "4":
                school.display_all_students()
            case "5":
                while True:
                    print(f"""
                    1 - Search student by ID
                    2 - Search student by name
                    3 - Cancel operation
                    """)
                    option = input("Enter your type of search: ")
                    if option == "1":
                        while True:   
                            try:
                                id_number = int(input("\nEnter student ID: "))
                                if school.find_student_by_id(id_number):
                                    menu2("student", id_number)
                                break
                            except ValueError:
                                print("\nInput must be a number")

                    elif option == "2":
                        student_name = input("Enter student's name: ")
                        if school.find_student_by_name(student_name):
                            menu2("student")
                    elif option == "3":
                        break
                    else:
                        print("Invalid input. Try again")
            case "6":
                while True:
                    print(f"""
                    1 - Search teacher by ID
                    2 - Search teacher by name
                    3 - Cancel operation
                    """)
                    option = input("Enter your type of search: ")
                    if option == "1":
                        while True:   
                            try:
                                id_number = int(input("\nEnter teacher ID: "))
                                if school.find_teacher_by_id(id_number):
                                    menu2("teacher", id_number)
                                break
                            except ValueError:
                                print("\nInput must be a number")                     

                    elif option == "2":
                        teacher_name = input("Enter teacher's name: ")
                        if school.find_teacher_by_name(teacher_name):
                            menu2("teacher")
                    elif option == "3":
                        break
                    else:
                        print("Invalid input. Try again")
            
            case "7":
                school.filter_teachers_by_subject(input("\nTeaching subject: "))
            case "8":
                school.filter_students_by_course(input("\nCourse name: "))
            case "9":
                print("Program ended.")
                break
            case _:
                print("Input not valid. Try again")

main()