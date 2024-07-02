from models import Person, Teacher, Student, School
from tools_management import read_json, write_json
from tools_management import menu2, input_menu
from tools_management import student_new_record, studentObject_to_Dict, teacher_new_record, teacherObject_to_Dict

# main function
def main(): 
    # Initializzation
    students_instances, teachers_instances, list_id = read_json()
    #create school instance with 2 arguments student_list and teachers_list
    school = School(students_instances, teachers_instances)

    # Initialize the ID
    Person.initialize_id(list_id)

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
                json_data = studentObject_to_Dict(students_instances) + teacherObject_to_Dict(teachers_instances)
                write_json(json_data, "New data added succesfully!")

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
                json_data = studentObject_to_Dict(students_instances) + teacherObject_to_Dict(teachers_instances)
                write_json(json_data, "New data added succesfully!")

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
                                    menu2(school, Student.profile, id_number)
                                break
                            except ValueError:
                                print("\nInput must be a number")

                    elif option == "2":
                        student_name = input("Enter student's name: ")
                        student_found, students_found_id =school.find_student_by_name(student_name)
                        if student_found:
                            menu2(school, Student.profile, students_found_id)
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
                                    menu2(school, Teacher.profile, id_number)
                                break
                            except ValueError:
                                print("\nInput must be a number")                     

                    elif option == "2":
                        teacher_name = input("Enter teacher's name: ")
                        teacher_found, teachers_found_id = school.find_teacher_by_name(teacher_name)
                        if teacher_found:
                            menu2(school, Teacher.profile, teachers_found_id)
                    elif option == "3":
                        break
                    else:
                        print("Invalid input. Try again")
            
            case "7":
                if(school.print_list_all_subjects()):
                    subject = input("\nEnter the subject for which you want to list the teachers: ")
                    teachers_by_subject = school.filter_teachers_by_subject(subject)
                    if teachers_by_subject != []: 
                        while True:
                            choice = input("Would you like to export the list to a JSON file? (Y/N) ")
                            if choice in "Yy":
                                message = f"\nTeachers list under {subject.upper()} created"
                                file_path = f"./data/list_teachers_{subject}.json"
                                write_json(teacherObject_to_Dict(teachers_by_subject), message, file_path)
                                break
                            elif choice in "Nn":
                                break
            case "8":
                if(school.print_list_all_courses()):
                    course = input("\nEnter the course for which you want to list the students: ")
                    students_by_course = school.filter_students_by_course(course)
                    if students_by_course != []:         
                        while True:
                            choice = input("Would you like to export the list to a JSON file? (Y/N) ")
                            if choice in "Yy":
                                message = f"\nStudents list under {course.upper()} created"
                                file_path = f"./data/list_students_{course}.json"
                                write_json(studentObject_to_Dict(students_by_course), message, file_path)
                                break
                            elif choice in "Nn":
                                break
            case "9":
                school.print_list_all_subjects()
            case "10":
                school.print_list_all_courses()
            case "11":
                print("Program ended")
                break
            case _:
                print("Input not valid. Try again")

if __name__ == "__main__":
    main()