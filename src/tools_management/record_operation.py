from models import Teacher, Student

def student_new_record():
    """
    It prompts the user to enter info like name, last name and address
    and collecting the input values it creates a Student object
    
    return student: the Student object just created
    """
    try: 
        while True:
            name = input("Enter name: ").strip().capitalize()
            if not name:
                print("Name cannot be empty")
            else:
                break      
        while True:
            last_name = input("Enter last name: ").strip().capitalize()
            if not last_name:
                print("Last name cannot be empty")
            else:
                break
        while True:
            address = input("Enter address: ").strip().capitalize()
            if not address:
                print("Address cannot be empty")
            else:
                break
        while True: 
            course = input("Enter course name: ").strip().capitalize()
            if not course:
                print("Course name cannot be empty")
            else:
                break
        # create an instance of the Student class
        student = Student(name, last_name, address, course)
        return student
    except AttributeError:
        print("Attribute assignment fails")
    except Exception as error:
        print(f"Unexpected error occurred: {error}")

def teacher_new_record():
    """
    It prompts the user to enter info like name, last name and address
    and collecting the input values it creates a Teacher object
    
    return: the Teacher object just created
    """
    try:
        while True:
            name = input("Enter name: ").strip().capitalize()
            if not name:
                print("Name cannot be empty")
            else:
                break
        while True:
            last_name = input("Enter last name: ").strip().capitalize()
            if not last_name:
                print("Last name cannot be empty")
            else:
                break
        while True:
            address = input("Enter address: ").strip().capitalize()
            if not address:
                print("Address cannot be empty")
            else:
                break
        while True:
            course = input("Enter teaching subject: ").strip().capitalize()
            if not course:
                print("Course  cannot be empty")
            else:
                break
        # create an instance of the Teacher class
        teacher = Teacher(name, last_name, address, course)
        return teacher
    except AttributeError:
        print("Attribute assignment fails")
    except Exception as error:
        print(f"Unexpected error occurred: {error}")

# converting students instances to dictionary
def studentObject_to_Dict(students): 
    """
    converts a list of Student objects into a list of dictionaries,
    following the key-value pairs of the object Student.
    
    parameters: students: list of Students instances
    
    return list_students: list of dictionaries. Each dictionary represent a Student object
    """
    list_students = []
    for i in students:
        try:
            # Create a dictionary for each Student instance with specific key-value pairs
            student_dict = {"#ID": i.get_id(),
                        "Name": i.name,
                        "Last name": i.last_name,
                        "Address": i.address,
                        "Course": i.course,
                        "Profile": i.profile
                        }
            # Append the dictionary representation of the Student object to the list
            list_students.append(student_dict)
        except AttributeError:
            print("Attribute reference fails")
        except KeyError:
            print("Dictionary key not found")
        except Exception as error:
            print(f"Unexpected error occurred: {error}")
    return list_students

# converting teachers instances to dictionary
def teacherObject_to_Dict(teachers):
    """
    converts a list of Teacher objects into a list of dictionaries,
    following the key-value pairs of the object Teacher.
    
    parameters: teacher: list of Teacher instances
    
    return list_teachers: list of dictionaries. Each dictionary represent a Teacher object
    """
    list_teachers = []
    for i in teachers:
        try:
            # Create a dictionary for each Teacher instance with specific key-value pairs
            teacher_dict = { "#ID": i.get_id(),
                        "Name": i.name,
                        "Last name": i.last_name,
                        "Address": i.address,
                        "Subject": i.subject_area,
                        "Profile": i.profile
            }
            # Append the dictionary representation of the Teacher object to the list
            list_teachers.append(teacher_dict)
        except AttributeError:
                print("Attribute reference fails")
        except KeyError:
                print("Dictionary key not found")
        except Exception as error:
                print(f"Unexpected error occurred: {error}")
    return list_teachers

def menu_search_student_teacher(school, entity_profile):
    """
    Displays a menu that allows users to search for students or teachers by ID or name.
    It executes the appropriate operation using methods from the school object and calling the 'menu_update_delete function'
    Based on the entity_profile, it performs operations on the students or teachers instances.

    parameters: school: An object containing methods for manipulating students and teachers instances
                entity_profile: An attribute indicating if the search is for a student or teacher
                Based on the entity_profile it performs operations on the students or teachers instances
    """
    while True:
                    # Display the menu options
                    print(f"""
                    1 - Search {entity_profile} by ID
                    2 - Search {entity_profile} by name
                    3 - Cancel operation
                    """)
                    # Prompt user for choice
                    choice = input("Enter your type of search: ")
                    
                    # Search by ID
                    if choice == "1":
                        while True:   
                            try:
                                # Prompt user for ID number
                                id_number = int(input(f"\nEnter {entity_profile} ID: "))
                                # If searching for a student, call find_student_by_id method
                                
                                if entity_profile == Student.profile:
                                    # If the method find_student_by_id returns True, 
                                    # call menu_update_delete function for further actions
                                    if school.find_student_by_id(id_number):
                                        menu_update_delete(school, Student.profile, id_number)
                                    break
                                # If searching for a teacher, call find_teacher_by_id method
                                
                                elif entity_profile == Teacher.profile:
                                    # If the method find_teacher_by_id returns True, 
                                    # call menu_update_delete function for further actions
                                    if school.find_teacher_by_id(id_number):
                                        menu_update_delete(school, Teacher.profile, id_number)
                                    break
                            except ValueError:
                                print("\nInput must be a number")
                    
                    # Search by name
                    elif choice == "2":
                        if entity_profile == Student.profile:
                            # If searching for a student, prompt user for student's name
                            student_name = input(f"Enter student's name: ")
                            # Call find_student_by_name method to find matching students
                            # this method returns a boolean True if at least one match is found and a list of id of the found students 
                            student_found, students_found_id = school.find_student_by_name(student_name)
                            
                           # If students_found == True, call menu_update_delete function for further actions
                            if student_found:
                                menu_update_delete(school, Student.profile, students_found_id)
                                
                        elif entity_profile == Teacher.profile:
                            # If searching for a teacher, prompt user for teacher's name
                            teacher_name = input("Enter teacher's name: ")
                            # Call find_teacher_by_name method to find matching teachers
                            # this method returns a boolean True if at least one match is found and a list of id of the found teachers 
                            teacher_found, teachers_found_id = school.find_teacher_by_name(teacher_name)
                            
                            # If teachers found == True, call menu_update_delete function for further actions
                            if teacher_found:
                                menu_update_delete(school, Teacher.profile, teachers_found_id)             
                    
                    elif choice == "3":
                        # Exit the loop if user chooses to cancel
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
        # Display sub-menu options
        print(f"""
        1 - Update {entity_profile} info
        2 - Delete {entity_profile} record
        3 - Back 
        """)
        choice = input("Enter your operation: ")

        if choice == "1":
             # If user chooses to update, call update_delete_records function with "update" operation
            update_delete_records(school, entity_profile, id, "update")
            break
                
        elif choice == "2":
            # If user chooses to delete, call update_delete_records function with "delete" operation
            update_delete_records(school, entity_profile, id, "delete")
            break
        elif choice == "3":
            # If user chooses to go back, exit the loop
            break
        else:
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
                operation (str): A string indicating the type of operation (update or delete).
    """
    # control if the ID parameter is a list type. 
    # If True means there could be more than one found record and 
    # it prompts the user to confirm the record's ID in case of namesakes
    if type(id) == list:
        while True:
            try:
                id_input = int(input("\nEnter ID to confirm the correct record to UPDATE in case there are namesakes: "))
                # If the id_input is found in the list `id`, proceed with the update or delete operation
                # of the student or teacher instance based on the entity_profile
                
                if id_input in id:
                    if entity_profile == Student.profile:
                            if operation == "update":
                                # Call school's student_update method with the ID
                                print(school.student_update(id_input))
                                break
                            elif operation == "delete":
                                # Call school's delete_student method with the ID
                                print(school.delete_student(id_input))
                                break
                    elif entity_profile == Teacher.profile:
                            if operation == "update":
                                # Call school's teacher_update method with the ID
                                print(school.teacher_update(id_input))
                                break
                            elif operation == "delete":
                                # Call school's delete_teacher method with the ID
                                print(school.delete_teacher(id_input))
                                break
                else:
                    print(f"\nID: {id_input} doesn't match any record from the search")
                    break
            except ValueError:
                print("\nInvalid input. Must be a number, try again")
    
    # control if the ID parameter is an integer type. 
    # If True directly perform the update or delete operation.
    # there is no need to prompt the user to confirm the ID since the serch was made by ID through
    # the find_student_by_id, find_teacher_by_id) method which returns only one ID

    if type(id) == int:
        if entity_profile == Student.profile:
            if operation == "update":
                # Call school's student_update method with the ID
                print(school.student_update(id))
            elif operation == "delete":
                # Call school's delete_student method with the ID
                print(school.delete_student(id))
            
        elif entity_profile == Teacher.profile:
            if operation == "update":
                # Call school's teacher_update method with the ID
                print(school.teacher_update(id))
            elif operation == "delete":
                # Call school's delete_teacher method with the ID
                print(school.delete_teacher(id))