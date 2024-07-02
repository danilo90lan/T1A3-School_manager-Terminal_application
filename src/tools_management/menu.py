from models import Student, Teacher

def menu2(school, entity_profile, id):
    print("What would you like to do?")   
    operation = True                    
    while operation:
        print(f"""
        1 - Update info
        2 - Delete record
        3 - Back 
        """)
        choice = input("Enter your operation: ")

        match choice:
            case "1":
                if type(id) == list:
                    while True:
                        try:
                            id_input = int(input("\nEnter ID to confirm the correct record(s) to UPDATE in case there are homonyms: "))
                            if id_input in id:
                                if entity_profile == Student.profile:
                                        school.student_update(id_input)
                                        operation = False
                                elif entity_profile == Teacher.profile:
                                        school.teacher_update(id_input)
                                        operation = False
                                break
                            else:
                                print("\nID doesn't match any record from the search")
                                operation = False
                                break
                        except ValueError:
                            print("\nInvalid input. Must be a number, try again")
                if type(id) == int:
                    if entity_profile == Student.profile:
                        school.student_update(id)
                        operation = False
                    elif entity_profile == Teacher.profile:
                        school.teacher_update(id)
                        operation = False

            case "2":
                if type(id) == list:
                    while True:
                        try:
                            id_input = int(input("Enter ID to confirm the correct record to DELETE in case there are homonyms: "))
                            if id_input in id:
                                if entity_profile == Student.profile:
                                        school.delete_student(id_input)
                                        operation = False

                                elif entity_profile == Teacher.profile:
                                        school.delete_teacher(id_input)
                                        operation = False
                                break
                            else:
                                print("\nID doesn't match any record from the search")
                                operation = False
                                break
                        except ValueError:
                            print("\nInvalid input. Must be a number, try again")

                
                elif type(id) == int: 
                    if entity_profile == Student.profile:
                        school.delete_student(id)
                        operation = False
                    elif entity_profile == Teacher.profile:
                        school.delete_teacher(id)
                        operation = False

            case "3":
                break
            case _:
                print("Invalid input. Try again")

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
                        7 - Filter teachers by teaching subject
                        8 - Filter students by course
                        9 - List all subjects
                       10 - List all courses
                       11 - Exit program
    """)
    return input("Enter your choice: ")
