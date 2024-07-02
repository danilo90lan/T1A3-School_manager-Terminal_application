from models import Teacher, Student

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

# converting students instances to dictionary
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

def menu_update_delete(school, entity_profile, id):
    from tools_management import update_delete_records
    print("What would you like to do?")                     
    while True:
        print(f"""
        1 - Update info
        2 - Delete record
        3 - Back 
        """)
        choice = input("Enter your operation: ")

        match choice:
            case "1":
                update_delete_records(school, entity_profile, id, "update")
                break
                
            case "2":
                update_delete_records(school, entity_profile, id, "delete")
                break
            case "3":
                break
            case _:
                print("Invalid input. Try again")

def update_delete_records(school, entity_profile, id, operation):
    if type(id) == list:
        while True:
            try:
                id_input = int(input("\nEnter ID to confirm the correct record(s) to UPDATE in case there are homonyms: "))
                if id_input in id:
                    if entity_profile == Student.profile:
                            if operation == "update":
                                school.student_update(id_input)
                                break
                            elif operation == "delete":
                                school.delete_student(id_input)
                                break
                    elif entity_profile == Teacher.profile:
                            if operation == "update":
                                school.teacher_update(id_input)
                                break
                            elif operation == "delete":
                                school.delete_teacher(id_input)
                                break
                else:
                    print("\nID doesn't match any record from the search")
                    break
            except ValueError:
                print("\nInvalid input. Must be a number, try again")
    
    if type(id) == int:
        if entity_profile == Student.profile:
            if operation == "update":
                school.student_update(id)
            elif operation == "delete":
                school.delete_student(id)
            
        elif entity_profile == Teacher.profile:
            if operation == "update":
                school.teacher_update(id)
            elif operation == "delete":
                school.delete_teacher(id)

# defining menu function
def input_menu():
    print("""
                        *************************************
                            WELCOME TO THE SCHOOL MANAGER
                        *************************************\
                        """)

    print(f"""
                        1 - Enter new teacher
                        2 - Enter new student
                        3 - Display teachers records (A - Z)
                        4 - Display students records (A - Z)
                        5 - Search student
                        6 - Search teacher
                        7 - Filter teachers by subject
                        8 - Filter students by course
                        9 - List all subjects
                       10 - List all courses
                       11 - Exit program
    """)
    return input("Enter your choice: ")
