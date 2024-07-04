from models import Student, Teacher
from tools_management import write_json, studentObject_to_Dict, teacherObject_to_Dict

class School: 
    """ The School class works as a container for instances of Student and Teacher objects, 
    providing methods to interact and manipulate these objects efficiently.
    """
    def __init__(self, students, teachers):
        """ The constructor initializes the class with two arguments: students and teachers, 
        which are lists containing student and teacher instances.
    """
        self.students = students
        self.teachers = teachers

    def display_all_students(self):
        """
        Sorts the student objects in alphabetical order.
        It uses the sorted function (which sorts the elemnts of students based on criteria 
        provided by the key parameter) and the lamba function that defines how each element should be 
        sorted. After the list of objects is sorted the method print_info is called which returns the 
        instance attributes values
        return: the number of the students instances
        """
        if self.students != []: 
            print(f"""
                            ***** List of all students *****\n""")
            # sort alphabetically
            sorted_students = sorted(self.students, key=lambda student: (student.name, student.last_name))
            for i in sorted_students:
                print(Student.print_info(i))
            return f"There are {len(sorted_students)} students registered in this school"
        else:
            return  "\nThere is no students records"

    def display_all_teachers(self):
        """
        Sorts the teacher objects in alphabetical order.
        It uses the sorted function (which sorts the elemnts of students based on criteria 
        provided by the key parameter) and the lamba function that defines how each element should be 
        sorted. After the list of objects is sorted the method print_info is called which returns the 
        instance attributes values
        return: the number of the teacher instances otherwise return another message
        """
        if self.teachers != []: 
            print(f"""
                            ***** List of all teachers *****\n""")
            # sort alphabetically
            sorted_teachers = sorted(self.teachers, key=lambda teacher: (teacher.name, teacher.last_name))
            for i in sorted_teachers:
                print(Teacher.print_info(i))
            return f"There are {len(sorted_teachers)} teachers registered in this school"
        else:
            return "\nThere is no teachers records"

    def find_student_by_id(self, student_id):
        """
        Finds a student by their ID number.
        parameter: student_id: an ID number to use for the search
        returns a boolean value True if the record is found, otherwise returns False.
        """
        record_found =False
        #Iterate through the student list and check if the ID provided 
        # by the parameter matches the ID of the instance. If so, set record_found = True."
        for i in self.students:
            if Student.get_id(i) == student_id:
                student = i
                record_found = True
                break
        if record_found:
            print(Student.print_info(student))
        else:
            print("\nStudent record NOT in the system")
        return record_found
    
    def find_student_by_name(self, student_name):
        """
        Finds students by a given name.
        Parameters: student_name: Name of the student to search for.
        Returns: student_record: boolean value True if students with the name are found, False otherwise.
                list: List of IDs of the students found with the matching name.
                (the return value is a list in case of namesakes)
        """
        student_record = False
        student_found = []
        for i in self.students:
            if i.name.lower() == student_name.lower():
                print(Student.print_info(i))
                student_found.append(Student.get_id(i))
                student_record = True
        if not student_record:
            print("\nStudent recond NOT in the system")
        return student_record, student_found

    def find_teacher_by_id(self, teacher_id):
        """
        Finds a student by their ID number.
        parameter: student_id: an ID number to use for the search
        returns a boolean value True if the record is found, otherwise returns False.
        """
        record_found = False
        for i in self.teachers:
            if Teacher.get_id(i) == teacher_id:
                teacher = i
                record_found = True
                break
        if record_found:
            print(Teacher.print_info(teacher))
        else:
            print("\nTeacher record NOT in the system")
        return record_found
    
    def find_teacher_by_name(self, teacher_name):
        """
        Finds teachers by a given name. 
        Parameters: teacher_name: Name of the teacher to search for.
        Returns: teacher_record: boolean value True if teachers with the name are found, False otherwise.
                list: List of IDs of the teachers found with the matching name.
                (the return value is a list in case of namesakes)
        """
        teacher_record = False
        teacher_found_id = []

        for i in self.teachers:
            if i.name.lower() == teacher_name.lower():
                print(Teacher.print_info(i))
                teacher_found_id.append(Teacher.get_id(i))
                teacher_record = True
        if not teacher_record:
            print("\nTeacher recond NOT in the system")
        return teacher_record, teacher_found_id

    def student_update(self, id):
        """
        Updates a student's information based on a given ID.
        if the id is found the update_student() method is called which update the
        instance in the student_list. Then it will be converted into a dictionary 
        by the function studentObject_to_Dict and then written again into the json file
        Parameters: id (int): ID of the student whose information is to be updated.
        """
        for i in self.students:
            if Student.get_id(i) == id:
                Student.update_student(i)
        # json data is the concatenation of two object lists (students and teachers)
        # that are converted into dictionaries
        json_data = studentObject_to_Dict(self.students) + teacherObject_to_Dict(self.teachers)
        write_json(json_data, f"\nThe student info with ID: {id} has beeen succesfully updated!")

    def teacher_update(self, id):
        """
        Updates a teacher's information based on a given ID.
        if the id is found the update_teacher() method is called which update the
        instance in the teacher_list. Then it will be converted into a dictionary 
        by the function studentObject_to_Dict and then written again into the json file
        Parameters: id (int): ID of the teacher whose information is to be updated.
        """
        for i in self.teachers:
            if Teacher.get_id(i) == id:
                Teacher.update_teacher(i)  
        # json data is the concatenation of two object lists (students and teachers)
        # that are converted into dictionaries
        json_data = studentObject_to_Dict(self.students) + teacherObject_to_Dict(self.teachers) 
        write_json(json_data,f"\nThe teacher info with ID: {id} has been succesfully updated!")

    def delete_teacher(self, id):
        for i in self.teachers:
            if Teacher.get_id(i) == id:
                self.teachers.remove(i)
        json_data = studentObject_to_Dict(self.students) + teacherObject_to_Dict(self.teachers)
        write_json(json_data, f"\nThe teacher record wih ID: {id} has been succesfully deleted!")

    def delete_student(self, id):
        for i in self.students:
            if Student.get_id(i) == id:
                self.students.remove(i)
        json_data = studentObject_to_Dict(self.students) + teacherObject_to_Dict(self.teachers)
        write_json(json_data, f"\n The student with ID: {id} has been succesfully deleted!")

    def filter_students_by_course(self, course):
        record = False
        list = []
        for i in self.students:
            if i.course.lower() == course.lower():
                list.append(i)
                print(Student.print_info(i))
                record = True
        if not record:
            print(f"\nThe course {course} has NOT been found in the system")
        return list
    
    def filter_teachers_by_subject(self, subject):
        record = False
        list = []
        for i in self.teachers:
            if i.subject_area.lower() == subject.lower():
                list.append(i)
                print(Teacher.print_info(i))
                record = True
        if not record:
            print(f"\nThe subject {subject} has NOT been found in the system")
        return list
    
    def print_list_all_courses(self):
        # defining a set variable to store the list of courses with no duplicate
        list_courses = set()
        # defining a boolean variable that returns False if the list is empty
        course = True

        for i in self.students:
            if i.course == "":
                continue
            list_courses.add(i.course)
        if list_courses:
            print(f"""
                    ***** List of all courses in the school *****\n""")
            for i in list_courses:
                print(i,"\n")
        else:
            print("There is NO courses in the system")
            course = False
        return course

    def print_list_all_subjects(self):
        # defining a set variable to store the list of all subjects with no duplicate
        list_subjects = set()
        # defining a boolean variable that returns False if the list is empty
        subject = True
        
        for i in self.teachers:
            if i.subject_area == "":
                continue
            list_subjects.add(i.subject_area)
        if list_subjects:
            print(f"""
                    ***** List of all subjects taught in the school *****\n""")
            for i in list_subjects:
                print(i,"\n")
        else:
            print("There is NO subjects in the system")
            subject = False
        return subject