from models import Teacher, Student

def student_new_record():
    """
    It prompts the user to enter info like name, last name and address
    and collecting the input values it creates a Student object
    return: the created Student object
    """
    name = input("Enter name: ").strip().capitalize()
    last_name = input("Enter last name: ").strip().capitalize()
    address = input("Enter address: ").strip().capitalize()
    course = input("Enter course name: ").strip().capitalize()
    student = Student(name, last_name, address, course)
    return student

def teacher_new_record():
    """
    It prompts the user to enter info like name, last name and address
    and collecting the input values it creates a Teacher object
    return: the created Teacher object
    """
    name = input("Enter name: ").strip().capitalize()
    last_name = input("Enter last name: ").strip().capitalize()
    address = input("Enter address: ").strip().capitalize()
    course = input("Enter teaching subject: ").strip().capitalize()
    teacher = Teacher(name, last_name, address, course)
    return teacher

# converting students instances to dictionary
def studentObject_to_Dict(students): 
    """
    converts a list of Student objects into a list of dictionaries,
    following the key-value pairs of the object Student.
    parameters: students: list of Students instances
    return: list of dictionaries. Each dictionary represent a Student object
    """
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
    """
    converts a list of Teacher objects into a list of dictionaries,
    following the key-value pairs of the object Teacher.
    parameters: teacher: list of Teacher instances
    return: list of dictionaries. Each dictionary represent a Teacher object
    """
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

def menu_search_student_teacher(school, entity_profile):
    """
    Displays a menu that allows users to search for students or teachers by ID or name.
    It executes the appropriate operation using methods from the school object and calling the 'menu_update_delete function'
    parameters: school: An object containing methods for manipulating students and teachers instances
                entity_profile: An attribute indicating if the search is for a student or teacher
                Based on the entity_profile it performs operations on the students or teachers instances
    """
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
                        # check if the object is either a student or teacher
                        if entity_profile == Student.profile:
                            student_name = input(f"Enter {entity_profile}'s name: ")
                            student_found, students_found_id = school.find_student_by_name(student_name)
                            # if the returned value student_found is True the function menu_update_delete is called
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
    """
    Displays a sub-menu that allows users to update or delete a student's or teacher's record.
    It executes the appropriate operation by calling the update_delete_records function.
    parameters: school: object containing methods for manipulating students and teachers instances
    such as updating and deleting records, entity_profile: an attribute indicating if the entity is a student 
    or teacher, id: ID number of the record that is going to be either updated or deleted
    """
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
    """
    Update or delete student or teacher records. 
    It handles scenarios where there are multiple possible namesakes by prompting the user to confirm the correct ID.
    It performs the operations (update or delete) using methods from the school object.
    parameters: school: School object containing methods for manipulating teachers and students instances,
    entity_profile: an attribute indicating if the entity is a student or teacher, 
    id: ID number of the record that is going to be either updated or deleted
    (could be either an integer or a list of integers based on the type of searching
    if the search was made by name (school.find_student_by_name) the ID is a list of integers in case of namesakes.
    But if the search was made by ID (school.find_student_by_id) the ID is an Integer.), 
    operation: A string indicating the type of operation (update or delete).
    """
    # control if the ID is a list type. 
    # If True means there could be more than one found record and 
    # it prompts the user to confirm the record's ID in case of namesakes
    if type(id) == list:
        while True:
            try:
                id_input = int(input("\nEnter ID to confirm the correct record to UPDATE in case there are namesakes: "))
                # if the id_input is found in the parameter id (which is a list) the methods 
                # students_delete , students_update or 
                # teachers_delete, teachers_update  will be called based on the entity_profile
                
                if id_input in id:
                    if entity_profile == Student.profile:
                            if operation == "update":
                                print(school.student_update(id_input))
                                break
                            elif operation == "delete":
                                print(school.delete_student(id_input))
                                break
                    elif entity_profile == Teacher.profile:
                            if operation == "update":
                                print(school.teacher_update(id_input))
                                break
                            elif operation == "delete":
                                print(school.delete_teacher(id_input))
                                break
                else:
                    print(f"\nID: {id_input} doesn't match any record from the search")
                    break
            except ValueError:
                print("\nInvalid input. Must be a number, try again")
    
    # control if the ID is an integer type. If True the methods students_delete , students_update or 
    # teachers_delete, teachers_update  will be called based on the entity_profile
    # there is no need to prompt the user to confirm the ID since the serch was made by ID through
    # the find_student_by_id, find_teacher_by_id) method which returns only one ID
    if type(id) == int:
        if entity_profile == Student.profile:
            if operation == "update":
                print(school.student_update(id))
            elif operation == "delete":
                print(school.delete_student(id))
            
        elif entity_profile == Teacher.profile:
            if operation == "update":
                print(school.teacher_update(id))
            elif operation == "delete":
                print(school.delete_teacher(id))