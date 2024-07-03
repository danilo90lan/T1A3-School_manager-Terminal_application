from models import Person, Teacher, Student, School
from tools_management import read_json, write_json
from tools_management import student_new_record, teacher_new_record, menu_search_student_teacher

# main function
def main(): 
    # Initializzation
    students_instances, teachers_instances, list_id = read_json()
    #create school instance with 2 arguments student_list and teachers_list
    school = School(students_instances, teachers_instances)

    # Initialize the ID
    Person.initialize_id(list_id)

    while True:
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
        choice = input("Enter your choice: ")
        
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
                menu_search_student_teacher(school, Student.profile)
            case "6":
                menu_search_student_teacher(school, Teacher.profile)
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