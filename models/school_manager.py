from models import Student, Teacher
from tools_management import write_json, student_object_to_dict, teacher_object_to_dict


class School:
    """ 
    The School class works as a container for instances of Student and Teacher objects, 
    providing methods to interact and manipulate these objects efficiently.
    """

    def __init__(self, students, teachers):
        """ 
        The constructor initializes the instance:  

        parameters:  students, teachers: list of student's instances and list of teacher's instances .
        """
        try:
            self.students = students
            self.teachers = teachers
        except AttributeError:
            print("Attribute assignment fails")
        except Exception as error:
            print(f"An expected error occured: {error}")

    def display_all_students(self):
        """
        Sorts the student objects in alphabetical order.
        It uses the sorted function (which sorts the elemnts of students based on criteria 
        provided by the key parameter) and the lamba function that defines how each element should be 
        sorted. After the list of objects is sorted the method print_info is called which returns the 
        instance attributes values

        return: the number of the students instances otherwise return another message
        """
        # check if the list of students is not empty
        if self.students != []:
            print(f"""
                            ***** LIST OF ALL STUDENTS *****\n""")
            try:
                # Sort students alphabetically by name and last name
                sorted_students = sorted(self.students, key=lambda student: (
                    student.name, student.last_name))
                for i in sorted_students:
                    # print each student's record by calling the print_info method()
                    print(Student.print_info(i))
                return f"There are {len(sorted_students)} students registered in this school"
            except TypeError:
                print(f"Cannnot get the length of {sorted_students}")
            except AttributeError as error:
                print(f"Attribute assignment fails {error}")
            except Exception as error:
                print(f"An expected error occured: {error}")

        else:
            return "\nThere is no students records"

    def display_all_teachers(self):
        """
        Sorts the teacher objects in alphabetical order.
        It uses the sorted function (which sorts the elemnts of students based on criteria 
        provided by the key parameter) and the lamba function that defines how each element should be 
        sorted. After the list of objects is sorted the method print_info is called which returns the 
        instance attributes values

        return: the number of the teacher instances otherwise return another message
        """
        # check if the list of teachers is not empty
        if self.teachers != []:
            print(f"""
                            ***** LIST OF ALL TEACHERS *****\n""")
            try:
                # Sort teachers alphabetically by name and last name
                sorted_teachers = sorted(self.teachers, key=lambda teacher: (
                    teacher.name, teacher.last_name))
                for i in sorted_teachers:
                    # print each teacher's record by calling the print_info method()
                    print(Teacher.print_info(i))
                return f"There are {len(sorted_teachers)} teachers registered in this school"
            except TypeError:
                print(f"Cannnot get the length of {sorted_teachers}")
            except AttributeError as error:
                print(f"Attribute assignment fails {error}")
            except Exception as error:
                print(f"An expected error occured: {error}")
        else:
            return "\nThere is no teachers records"

    def find_student_by_id(self, student_id):
        """
        Finds a student by their ID number.

        parameter: student_id: an ID number to use for the search

        returns: record_found: a boolean value True if the record is found, otherwise returns False.
        """
        record_found = False
        # Iterate through the student list and check if the ID provided
        # by the parameter matches the ID of the instance. If so, set record_found = True."
        try:
            for i in self.students:
                # Check if the ID of the current student matches the provided student_id
                if Student.get_id(i) == student_id:
                    # If a match is found, set record_found to True and store the student instance
                    student = i
                    record_found = True
                    break
            # If a student record is found, print its information using Student.print_info method
            if record_found:
                print(Student.print_info(student))
            else:
                print("\nStudent record NOT in the system")
        except Exception as error:
            print(f"An expected error occured: {error}")
        return record_found

    def find_student_by_name(self, student_name):
        """
        Finds students by a given name.

        Parameters: student_name: Name of the student to search for.

        Returns: student_record: boolean value True if students with the name are found, False otherwise.
                list: List of IDs of the students found with the matching name.
                (the return value is a list in case of namesakes)
        """
        # boolean flag to track if any student records are found
        student_record = False
        # Initialize an empty list to store IDs of students found with matching name
        student_found = []
        try:
            for i in self.students:
                # Check if the student's name matches the search name
                if i.name.lower() == student_name.lower():
                    # If a match is found, print the student's information using Student.print_info method
                    print(Student.print_info(i))
                    # Append the ID of the matched student to the student_found list
                    student_found.append(Student.get_id(i))
                    # Set student_record to True indicating that at least one student with the name was found
                    student_record = True
            # If no student records are found with the given name print the message
            if not student_record:
                print("\nStudent recond NOT in the system")
            # Return the boolean flag indicating if records were found and the list of IDs of matching students
        except Exception as error:
            print(f"An expected error occured: {error}")
        return student_record, student_found

    def find_teacher_by_id(self, teacher_id):
        """
        Finds a student by their ID number.

        parameter: student_id: an ID number to use for the search

        returns a boolean value True if the record is found, otherwise returns False.
        """
        # Initialize a boolean flag to track if the teacher record is found
        record_found = False
        try:
            for i in self.teachers:
                # Check if the ID of the current teacher matches the provided teacher_id
                if Teacher.get_id(i) == teacher_id:
                    # Set record_found to True indicating that the teacher record was found and store teacher instance
                    teacher = i
                    record_found = True
                    break
            # If no teacher record is found with the given ID, print a message
            if record_found:
                print(Teacher.print_info(teacher))
            else:
                print("\nTeacher record NOT in the system")
            # Return the boolean flag indicating if the record was found
        except Exception as error:
            print(f"An expected error occured: {error}")
        return record_found

    def find_teacher_by_name(self, teacher_name):
        """
        Finds teachers by a given name. 

        Parameters: teacher_name: Name of the teacher to search for.

        Returns: teacher_record: boolean value True if teachers with the name are found, False otherwise.
        list: List of IDs of the teachers found with the matching name.
        (the return value is a list in case of namesakes)
        """
        # Initialize a boolean flag to track if the teacher record is found
        teacher_record = False
        # Initialize an empty list to store IDs of teachers found with matching name
        teacher_found_id = []
        try:
            for i in self.teachers:
                # # Check if the teacher's name matches the search name
                if i.name.lower() == teacher_name.lower():
                    # If a match is found, print the teacher's information using Teacher.print_info
                    print(Teacher.print_info(i))
                    # Add the ID of the found teacher to teacher_found_id list using Teacher.get_id
                    teacher_found_id.append(Teacher.get_id(i))
                    # Set teacher_record to True indicating that at least one teacher record was found
                    teacher_record = True
            # If no teacher records are found with the given name, print a message
            if not teacher_record:
                print("\nTeacher recond NOT in the system")
        except Exception as error:
            print(f"An expected error occured: {error}")
        return teacher_record, teacher_found_id

    def student_update(self, id):
        """
        Updates a student's information based on a given ID.
        if the id is found the update_student() method is called which update the
        instance in the student_list. Then it will be converted into a dictionary 
        by the function studentObject_to_Dict and then written again into the json file

        Parameters: id (int): ID of the student whose information is to be updated.

        return: a string with containing a message of succesfully updating
        """
        try:
            for i in self.students:
                if Student.get_id(i) == id:
                    Student.update_student(i)
            # Concatenate the dictionaries of students and teachers into json_data
            # by converting it into dictionaries using the studentObject_to_Dict and the teacherObject_to_Dict functions
            json_data = student_object_to_dict(
                self.students) + teacher_object_to_dict(self.teachers)
            # Write the updated data back to the JSON file
            try:
                write_json(json_data)
            except Exception as error:
                print(f"Error saving data: {error}")
            return f"\nThe student info with ID: {id} has beeen succesfully updated!"
        except Exception as error:
            print(f"An expected error occured: {error}")

    def teacher_update(self, id):
        """
        Updates a teacher's information based on a given ID.
        if the id is found the update_teacher() method is called which update the
        instance in the teacher_list. Then it will be converted into a dictionary 
        by the function studentObject_to_Dict and then written again into the json file

        Parameters: id (int): ID of the teacher whose information is to be updated.

        return: a string with containing a message of succesfully updating
        """
        try:
            for i in self.teachers:
                if Teacher.get_id(i) == id:
                    Teacher.update_teacher(i)
            # Concatenate the dictionaries of students and teachers into json_data
            # by converting it into dictionaries using the studentObject_to_Dict and the teacherObject_to_Dict functions
            json_data = student_object_to_dict(
                self.students) + teacher_object_to_dict(self.teachers)
            # Write the updated data back to the JSON file
            try:
                write_json(json_data)
            except Exception as error:
                print(f"Error saving data: {error}")
            return f"\nThe teacher info with ID: {id} has been succesfully updated!"
        except Exception as error:
            print(f"An expected error occured: {error}")

    def delete_teacher(self, id):
        try:
            for i in self.teachers:
                # if the given id matches the teacher id, the instance will be removed from the list
                if Teacher.get_id(i) == id:
                    self.teachers.remove(i)
            # Concatenate the dictionaries of students and teachers into json_data
            # by converting it into dictionaries using the studentObject_to_Dict and the teacherObject_to_Dict functions
            json_data = student_object_to_dict(
                self.students) + teacher_object_to_dict(self.teachers)
            # Write the updated data back to the JSON file
            try:
                write_json(json_data)
            except Exception as error:
                print(f"Error saving data: {error}")
            return f"\nThe teacher record wih ID: {id} has been succesfully deleted!"
        except Exception as error:
            print(f"An expected error occured: {error}")

    def delete_student(self, id):
        try:
            for i in self.students:
                # if the given id matches the student id, the instance will be removed from the list
                if Student.get_id(i) == id:
                    self.students.remove(i)
            # Concatenate the dictionaries of students and teachers into json_data
            # by converting it into dictionaries using the studentObject_to_Dict and the teacherObject_to_Dict functions
            json_data = student_object_to_dict(
                self.students) + teacher_object_to_dict(self.teachers)
            # Write the updated data back to the JSON file
            try:
                write_json(json_data)
            except Exception as error:
                print(f"Error saving data: {error}")
            return f"\n The student with ID: {id} has been succesfully deleted!"
        except Exception as error:
            print(f"An expected error occured: {error}")

    def filter_students_by_course(self, course):
        """
        Filters and retrieves students enrolled in a specified course.

        Parameters:
        course (str): The name of the course to filter students by.

        Returns:
        list: A list of students who are enrolled in the specified course.
        """
        # Flag to track if any students are found
        record = False
        # List to store students enrolled in the specified course
        list = []
        try:
            for i in self.students:
                # Check if the student's course matches the specified course
                if i.course.lower() == course.lower():
                    # Add student to the list
                    list.append(i)
                    # print student information by calling the print_info method
                    print(Student.print_info(i))
                    record = True
            if not record:
                print(
                    f"\nThe course {course} has NOT been found in the system")
            return list
        except AttributeError as error:
            print(f"Attribute reference fails {error}")
        except Exception as error:
            print(f"An expected error occured: {error}")

    def filter_teachers_by_subject(self, subject):
        """
        Filters and retrieves teachers who teach a specified subject.

        Parameters:
        subject (str): The name of the subject to filter teachers by.

        Returns:
        list: A list of teachers who teach the specified subject.
        """
        # Flag to track if any teachers are found
        record = False
        # List to store teachers who teach the specified subject
        list = []
        try:
            for i in self.teachers:
                # Check if the teacher's subject area matches the specified subject
                if i.subject_area.lower() == subject.lower():
                    # Add teacher to the list
                    list.append(i)
                    # Print teacher information by calling print_info method
                    print(Teacher.print_info(i))
                    record = True
            if not record:
                print(
                    f"\nThe subject {subject} has NOT been found in the system")
            return list
        except AttributeError as error:
            print(f"Attribute reference fails {error}")
        except Exception as error:
            print(f"An expected error occured: {error}")

    def print_list_all_courses(self):
        """
        Prints a list of all unique courses taken by students in the school.

        Returns:
        bool: True if there are courses in the system, False otherwise.
        """
        try:
            # defining a set variable to store the list of courses with no duplicate
            list_courses = set()
            # defining a boolean variable that returns False if the list is empty
            course = True
            for i in self.students:
                try:
                    # Skip students with an empty course attribute
                    if i.course == "":
                        continue
                    # Add the student's course to the set of courses
                    list_courses.add(i.course)
                except AttributeError as error:
                    # if the attribute is not accesible will be skip it
                    print("Course attribute is not accessible")
                    continue
            # Check if any courses were found
            if list_courses:
                print(f"""
                        ***** LIST OF ALL COURSES *****\n""")
                # Print each course in the set
                for i in list_courses:
                    print(i, "\n")
            else:
                print("There is NO courses in the system")
                # Set the boolean variable to False if no courses were found
                course = False
            return course
        except Exception as error:
            print(f"An expected error occured: {error}")

    def print_list_all_subjects(self):
        """
        Prints a list of all unique subjects taught by teachers in the school.

        Returns:
        bool: True if there are subjects in the system, False otherwise.
        """
        try:
            # defining a set variable to store the list of all subjects with no duplicate
            list_subjects = set()
            # defining a boolean variable that returns False if the list is empty
            subject = True

            for i in self.teachers:
                try:
                    # Skip teachers with an empty subject_area attribute
                    if i.subject_area == "":
                        continue
                    # Add the teacher's subject_area to the set of subjects
                    list_subjects.add(i.subject_area)
                except AttributeError as error:
                    # if the attribute is not accesible will be skip it
                    print("Course attribute is not accessible")
                    continue
            # Check if any subjects were found
            if list_subjects:
                print(f"""
                        ***** LIST OF ALL SUBJECTS *****\n""")
                # Print each subject in the set
                for i in list_subjects:
                    print(i, "\n")
            else:
                print("There is NO subjects in the system")
                # Set the boolean variable to False if no subjects were found
                subject = False
            return subject
        except Exception as error:
            print(f"An expected error occured: {error}")
