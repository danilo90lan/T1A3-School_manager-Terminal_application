from datetime import datetime
from models import Person, Teacher, Student, School
from tools_management import read_json, write_json, student_object_to_dict, teacher_object_to_dict
from tools_management import student_new_record, teacher_new_record, menu_search_student_teacher
import sys


def prompting_user(message):
    """
    keep prompting the user till get a valid response of either 'Y' (yes) or 'N' (no)

    parameter: message: string containing the message to visualize to the user

    return: the valid input choice.
    """
    choice = input(message)
    while choice not in "YyNn":
        choice = input(
            "Invalid input. Please enter Y or N: ")
    return choice

# main function


def main():
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]

    print("The arguments are ", arg1, arg2)

    """
    Initialization of students and teachers records based on the json file.
    Initialization of the ID system based on the JSON file to ensure each record has a unique ID
    Interacting with the user through a menu system, allowing the user to perform various actions
    like adding and displaying records, searching, filtering, and listing subjects and courses
    """

    # Initializzation
    """initializing three variables from JSON file:
    students_instances: A list of student objects.
    teachers_instances: A list of teacher objects.
    list_id: A list of ID used for initializing person IDs."""
    try:
        students_instances, teachers_instances, list_id = read_json()
        # creates an object of the School class with the students_instances and
        # teachers_instances as attributes.
        school = School(students_instances, teachers_instances)
    except Exception as error:
        print(f"An expected error occured: {error}")

    # initializes the ID for Person objects using the list of IDs from the
    # JSON file.
    Person.initialize_id(list_id)

    # get the current date and convert it into a string
    # the date is used as part of the file name .json after the creation
    # of the list of students or teachers under a specific subject or course
    # name
    try:
        current_date = datetime.now().strftime("%d-%m-%Y")
    except TypeError as error:
        print(
            f"Error occurred while getting or formatting current date: {error}")

    # defining vriables containing messages to pass as arguments to avoid redundancy across the main()
    message_export_json_list = "Would you like to export the list to a JSON file? (Y/N) "
    message_enter_new_record = "\nDo you want to enter another one? (Y/N) "

    while True:
        # Displaying the main menu options
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
        #  prompt the user to perform an operation
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                new_record = "Y"
                try:
                    while new_record in ("Yy"):
                        # create a new Teacher instance by calling the
                        # teacher_new_record() function
                        new_teacher = teacher_new_record()
                        # append the new Teacher instance to the teachers list
                        teachers_instances.append(new_teacher)
                        # call promptin_user function to ask the user if wants to enter a new record
                        new_record = prompting_user(message_enter_new_record)
                    # concatenate list students and list teachers after
                    # converting them into a lisgt of dictionaries
                    json_data = student_object_to_dict(
                        students_instances) + teacher_object_to_dict(teachers_instances)
                except Exception as error:
                    print(f"An expected error occured: {error}")
                # write the new lists to json file after adding all new records
                try:
                    write_json(json_data, "New data added succesfully!")
                except Exception as error:
                    print(f"Error saving data: {error}")

            case "2":
                new_record = "Y"
                try:
                    while new_record in ("Yy"):
                        # create a new Student instance by calling the
                        # teacher_new_record() function
                        new_student = student_new_record()
                        # update the new Student instance to the students list
                        students_instances.append(new_student)
                        # call promptin_user function to ask the user if wants to enter a new record
                        new_record = prompting_user(message_enter_new_record)
                    # concatenate list students and list teachers after
                    # converting them into a lisgt of dictionaries
                    json_data = student_object_to_dict(
                        students_instances) + teacher_object_to_dict(teachers_instances)
                except Exception as error:
                    print(f"An expected error occured: {error}")
                # write the new lists to json file after adding all new records
                try:
                    write_json(json_data, "New data added succesfully!")
                except Exception as error:
                    print(f"Error saving data: {error}")

            case "3":
                try:
                    # Displaying all teachers by calling the method
                    # display_all_teachers()
                    print(school.display_all_teachers())
                except Exception as error:
                    print(f"An expected error occured: {error}")
            case "4":
                try:
                    # Displaying all students by calling the method
                    # display_all_students()
                    print(school.display_all_students())
                except Exception as error:
                    print(f"An expected error occured: {error}")
            case "5":
                try:
                    # Searching for a student by ID or name by calling the menu_search_student_teacher() method
                    # the argument is Student.profile in order to perform the
                    # opeartions on the student list
                    menu_search_student_teacher(school, Student.PROFILE)
                except Exception as error:
                    print(f"An expected error occured: {error}")
            case "6":
                try:
                    # Searching for a student by ID or name by calling the menu_search_student_teacher() method
                    # the argument is Teacher.profile in order to perform the
                    # opeartions on the teachers list
                    menu_search_student_teacher(school, Teacher.PROFILE)
                except Exception as error:
                    print(f"An expected error occured: {error}")
            case "7":
                # Filtering teachers by subject and optionally exporting to a
                # new JSON file
                try:
                    # if print_list_all_subjects() == True prompt the user to
                    # enter the subject name to search for
                    if (school.print_list_all_subjects()):
                        subject = input(
                            "\nEnter the subject for which you want to list the teachers: ").strip()

                        # store in the teachers_by_subject variable the returned list from
                        # the filter_teachers_by_subject method which has the
                        # user's prompt as argument
                        teachers_by_subject = school.filter_teachers_by_subject(
                            subject)

                        # if the teachers_by_subject variable is not empty
                        # it prompt the user is wants to export the list into a
                        # new json file
                        if teachers_by_subject != []:
                            # call promptin_user function to ask the user if wants export the list to new different JSON file
                            if prompting_user(message_export_json_list) in "Yy":
                                message = f"\nTeachers list under {subject.upper()} created"
                                # the filename of the new JSON file will be
                                # thw current date + the {subject}
                                file_path = f"./data/{current_date}_teachers_{subject}_.json"

                                # converts the subject list into dictionaries and pass it to write_json
                                # along with the customized message and the
                                # new file path as arguments
                                try:
                                    write_json(
                                        teacher_object_to_dict(teachers_by_subject), message, file_path)
                                except Exception as error:
                                    print(f"Error saving data: {error}")
                except Exception as error:
                    print(f"An expected error occured: {error}")
            case "8":
                # Filtering students by course and optionally exporting to JSON
                try:
                    # if print_list_all_courses() == True prompt the user to
                    # enter the course name to search for
                    if (school.print_list_all_courses()):
                        course = input(
                            "\nEnter the course for which you want to list the students: ").strip()

                        # store in the students_by_course variable the returned list from
                        # the filter_students_by_course method which has the
                        # user's prompt as argument
                        students_by_course = school.filter_students_by_course(
                            course)

                        # if the teachers_by_subject variable is not empty
                        # it prompt the user is wants to export the list into a
                        # new json file

                        if students_by_course != []:
                            # call promptin_user function to ask the user if wants export the list to new different JSON file
                            if prompting_user(message_export_json_list) in "Yy":
                                message = f"\nStudents list under {course.upper()} created"
                                # the filename of the new JSON file will be
                                # thw current date + the {course}
                                file_path = f"./data/{current_date}_students_{course}.json"

                                # converts the course list into dictionaries and pass it to write_json
                                # along with the customized message and the
                                # new file path as arguments
                                try:
                                    write_json(
                                        student_object_to_dict(students_by_course), message, file_path)
                                except Exception as error:
                                    print(f"Error saving data: {error}")
                except Exception as error:
                    print(f"An expected error occured: {error}")
            case "9":
                # Listing all subjects taught in the school by calling the
                # print_list_all_subjects() mwthod
                try:
                    school.print_list_all_subjects()
                except Exception as error:
                    print(f"An expected error occured: {error}")
            case "10":
                # Listing all courses available in the school by calling the
                # print_list_all_courses() method
                try:
                    school.print_list_all_courses()
                except Exception as error:
                    print(f"An expected error occured: {error}")
            case "11":
                # Exiting the program
                print("Program ended")
                break
            case _:
                print("Input not valid. Try again")


if __name__ == "__main__":
    main()
