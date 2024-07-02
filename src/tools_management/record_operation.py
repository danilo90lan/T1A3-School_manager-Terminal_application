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

def menu_search_student_teacher(school, entity_profile):
    while True:
                    print(f"""
                    1 - Search {entity_profile} by ID
                    2 - Search {entity_profile} by name
                    3 - Cancel operation
                    """)
                    choice = input("Enter your type of search: ")
                    if choice == "1":
                        while True:   
                            try:
                                id_number = int(input(f"\nEnter {entity_profile} ID: "))
                                if entity_profile == Student.profile:
                                    if school.find_student_by_id(id_number):
                                        menu_update_delete(school, Student.profile, id_number)
                                    break
                                elif entity_profile == Teacher.profile:
                                    if school.find_teacher_by_id(id_number):
                                        menu_update_delete(school, Teacher.profile, id_number)
                                    break
                            except ValueError:
                                print("\nInput must be a number")

                    elif choice == "2":
                        if entity_profile == Student.profile:
                            student_name = input(f"Enter {entity_profile}'s name: ")
                            student_found, students_found_id = school.find_student_by_name(student_name)
                            if student_found:
                                menu_update_delete(school, Student.profile, students_found_id)
                        elif entity_profile == Teacher.profile:
                            teacher_name = input("Enter teacher's name: ")
                            teacher_found, teachers_found_id = school.find_teacher_by_name(teacher_name)
                            if teacher_found:
                                menu_update_delete(school, Teacher.profile, teachers_found_id)
                            
                    elif choice == "3":
                        break
                    else:
                        print("Invalid input. Try again")

def menu_update_delete(school, entity_profile, id):
    print("What would you like to do?")                     
    while True:
        print(f"""
        1 - Update {entity_profile} info
        2 - Delete {entity_profile} record
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
                id_input = int(input("\nEnter ID to confirm the correct record to UPDATE in case there are homonyms: "))
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
                    print(f"\nID: {id_input} doesn't match any record from the search")
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